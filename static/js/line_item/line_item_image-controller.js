/**
angular.module('manpower').config(function (LightboxProvider) {

  // our images array is not in the default format, so we have to write this
  // custom method
  LightboxProvider.getImageUrl = function (imageUrl) {
    return imageUrl;
  };

  // set the caption of each image as its text color
  LightboxProvider.getImageCaption = function (imageUrl) {
    return '#' + imageUrl.match(/00\/(\w+)/)[1];
  };

});
*/
angular.module('manpower').controller('LineItemImageController', function ($scope, Lightbox, Restangular, $q, $upload ) {
  $scope.Lightbox = Lightbox;

  $scope.files ={};
  $scope.init = function(li_id){
    Restangular.one('api/line_item', li_id).get()
    .then( function(li){
      $scope.currentLineItem = li;
      console.log("got li!");
      console.log(JSON.stringify(li));
      $scope.getImages();
    });
  }

  
  $scope.images=[];
  $scope.getImages = function(){
    Restangular.one('getS3prefix').get()
    .then( function(res){
      return res;
    })
    .then( function( pfx ){
      $scope.bucket = pfx;
      return $scope.currentLineItem.getList('images');
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
          postObj["lineitem_id"] = $scope.currentLineItem.id;
          postObj["project_id"] = $scope.currentLineItem.project_id;
          Restangular.all('api/site_image').post(postObj)
          .then(function( newimg ){
            $scope.addImage( newimg );
          });

        });
      });
    };
  }

});
