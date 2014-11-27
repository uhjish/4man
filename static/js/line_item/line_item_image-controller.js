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
  $scope.images=[];
  $scope.addSlide = function() {
    var newWidth = 600 + $scope.images.length + 1;
    $scope.images.push({
      url: 'http://placekitten.com/' + newWidth + '/300',
      caption: ['More','Extra','Lots of','Surplus'][$scope.images.length % 4] + ' ' +
        ['Cats', 'Kittys', 'Felines', 'Cutes'][$scope.images.length % 4]
    });
  };
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
    for (var i=0; i<4; i++) {
      $scope.addSlide();
    }

  }

  $scope.openLightboxModal = function (index) {
    console.log(JSON.stringify($scope.images[index]));
    Lightbox.openModal($scope.images, index);
  };
});
