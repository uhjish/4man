angular.module('manpower').
  controller("ProjectListController",function($q, Restangular,$scope, $filter, $http, $location, $upload){

  var resource = Restangular.all('api/project')
  resource.getList().then(function(projects){
    $scope.projects = projects;
  });

  $scope.viewProject = function( project_id ){
    console.log("project:" + project_id);
    $location.path( 'project/' + project_id )
  }

  $scope.onFileSelect = function($files, project_id) {
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
          postObj["project_id"] = project_id;
          Restangular.all('api/site_image').post(postObj)
          .then(function( newimg ){
            console.log( "new image added: " + newimg.image_uuid );
          });

        });
      });
    };
  }
});
