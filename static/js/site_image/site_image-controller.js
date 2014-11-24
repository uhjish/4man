
angular.module('manpower').
  controller("SiteImageController",function(Restangular,$scope, $filter){

  $scope.init=function(img_list){
    $scope.images = img_list;
    Restangular.one('api/site_image_url').get().then( function(result){
      $scope.site_image_url = result;
    });
  };

  $scope.getImageURL = function( img ){
    return $scope.site_image_url + "/" + img.image_uuid + "." + img.image_ext;
  }

}
