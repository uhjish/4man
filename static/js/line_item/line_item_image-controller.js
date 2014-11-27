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

angular.module('manpower').controller('LineItemImageController', function ($scope, Lightbox, Restangular, $q) {
  $scope.Lightbox = Lightbox;

  $scope.init = function(li_id){
    Restangular.one('api/line_item', li_id).get()
    .then( function(li){
      $scope.currentLineItem = li;
      console.log("got li!");
      console.log(JSON.stringify(li));
      $scope.getImages();
    });
  }

  images = [
    {
    'url': 'http://upload.wikimedia.org/wikipedia/commons/8/87/Waynejunction0810b.JPG',
    'caption': 'This image has dimensions 2272x1704 and the img element is scaled to fit inside the window. The left and right arrow keys are binded for navigation. The escape key for closing the modal is binded by AngularUI Bootstrap.'
  },
  {
    'url': 'http://upload.wikimedia.org/wikipedia/commons/thumb/9/98/%27Grand_Canyon_with_Rainbow%27_by_Thomas_Moran%2C_1912.JPG/586px-%27Grand_Canyon_with_Rainbow%27_by_Thomas_Moran%2C_1912.JPG',
    'caption': 'This image has dimensions 586x480.'
  },
  {
    'url': 'http://upload.wikimedia.org/wikipedia/commons/8/82/%27Right_Shoulder%2C_Arm%2C_and_Hand%27_by_Thomas_Eakins.JPG',
    'caption': 'This image has dimensions 975x3105.'
  }];

  $scope.getImages = function(){
    Restangular.one('getS3prefix').get()
    .then( function(res){
      return res;
    })
    .then( function( pfx ){
      $scope.pfx = pfx;
      return $scope.currentLineItem.getList('images');
    })
    .then(function(results){
      results.forEach( function(img){
        img.url = $scope.pfx + $img.image_uuid + "." + $img.image_ext;
        img.caption = "blah";
      });
    });
    $scope.images = images;
  }

  $scope.openLightboxModal = function (index) {
    console.log(JSON.stringify($scope.images[index]));
    Lightbox.openModal($scope.images, index);
  };
});
