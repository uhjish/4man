
angular.module('manpower').controller('ProjectImageController', function ($scope, Lightbox, Restangular, $q, $upload) {
  $scope.Lightbox = Lightbox;

  $scope.files ={};
  $scope.init = function(){
    $scope.images = [];
    $scope.getCurrentProject()
    .then(function(currentProject){
      $scope.project_id = currentProject.id;
      $scope.lineitems = currentProject.line_items;
      console.log(JSON.stringify(currentProject));
      $scope.getImages(currentProject);
    });
  }

  $scope.getCurrentProject = function() {
    var deferred = $q.defer();
    $scope.$watch('currentProject', function(val) {
      if (val){
        deferred.resolve(val);
        console.log("found "+ val.shortname);
      }
    });
    return deferred.promise;
  };
  
  $scope.images=[];
  $scope.getImages = function(currentProject){
    Restangular.one('getS3prefix').get()
    .then( function(res){
      return res;
    })
    .then( function( pfx ){
      $scope.bucket = pfx;
      return $scope.currentProject.getList('images');
    })
    .then(function(results){
      results.forEach( function(img){
        $scope.addImage(img);
      });
    });
  }

  $scope.addImage = function(img){
    img["url"] = $scope.bucket + img.image_uuid;
    img["caption"] = img.created_at.substring(0,10);
    $scope.images.push(img); 
  
  }

  $scope.refreshImages = function(){
    $scope.init()
  }

  $scope.updateImageLineItem = function(idx, newLI){
    var id = $scope.images[idx].image_uuid;
    console.log("id: " + JSON.stringify($scope.images[idx]));
    console.log("li: " + newLI);
    Restangular.one('api/site_image', id).customPUT({"lineitem_id": newLI})
    .then( function( newImg ) {
      newImg["url"] = $scope.bucket + newImg.image_uuid;
      newImg["caption"] = newImg.created_at.substring(0,10);
      $scope.images[idx] = newImg;
    });
  }

  $scope.deleteLineItemImage = function(idx){
    var del_id = $scope.images[idx].image_uuid;
    console.log( "deleting image id: " + del_id + " --" + idx );
    Restangular.one('api/site_image', del_id).remove()
    .then( function() {
      console.log("All ok");
      $scope.images.splice(idx,1);
    }, function(response) {
      console.log("Error with status code", response.status);
    });
  }

  $scope.openLightboxModal = function (index) {
    console.log(JSON.stringify($scope.images[index]));
    Lightbox.openModal($scope.images, index);
  };

  $scope.onFileSelect = function($files) {
    //$files: an array of files selected, each file has name, size, and type.
    for (var i = 0; i < $files.length; i++) {
      var file = $files[i];
      Restangular.one('getS3access').get()
      .then( function( imgToken ) {
        file.uuid = imgToken.file_id;
        $scope.upload = $upload.upload({
          url: 'https://4man-static-storage.s3.amazonaws.com/', 
          method: 'POST',
          data : {
            key: "project-images/" + imgToken.file_id,
            AWSAccessKeyId: imgToken.key, 
            policy: imgToken.policy,
            signature: imgToken.signature, 
            "Content-Type": file.type != '' ? file.type : 'application/octet-stream', 
          },
          file: file,
        }).progress(function(evt) {
          console.log('percent: ' + parseInt(100.0 * evt.loaded / evt.total));
        }).success(function(data, status, headers, config) {
          // file is uploaded successfully
          console.log(data);
          var postObj = {};
          postObj["image_uuid"] = file.uuid;
          postObj["project_id"] = $scope.currentProject.id;
          Restangular.all('api/site_image').post(postObj)
          .then(function( newimg ){
            $scope.addImage( newimg );
          });

        });
      });
    };
  }

});
