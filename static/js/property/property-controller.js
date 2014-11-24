
angular.module('manpower').
  controller("PropertyController",function($q, Restangular,$scope, $filter, $http, $modal){

  $scope.init=function(){
    $scope.getCurrentProject().then(function(val){
      $scope.property_id = val.property_id;
      Restangular.one('api/property', $scope.property_id).get().then( function (result){
        $scope.currentProperty = result;
        console.log(JSON.stringify(result));
        $scope.getGMapsURL();
      });
    })
  };

  $scope.alerts=[];
  $scope.addAlert = function(text) {
    return $scope.alerts.push({msg: text}) - 1;
  };

  $scope.closeAlert = function(index) {
    $scope.alerts.splice(index, 1);
  };

  $scope.fadingAlert =function(text, delay) {
    delay = typeof delay !== 'undefined' ? delay : 2000;
    var alertIdx = $scope.addAlert(text);
    window.setTimeout(function() {
      $scope.closeAlert( alertIdx );
    }, delay);
  };

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

  $scope.validateAddress = function( street, city, state ){
    var addr = street+" "+city+", "+state;
    addr = "address="+encodeURIComponent(addr);
    console.log(addr);
    $http.get('https://maps.googleapis.com/maps/api/geocode/json?'+addr).
    success(function(data){
      console.log(JSON.stringify(data));
      if (data.status == "ZERO_RESULTS"){
        console.log("invalid address!");
        $scope.fadingAlert('Invalid address! Try again.');
        return -1;
      }
      if (data.results.length > 1){
        //ambiguous address
        // create selector
      }
      res = data.results[0].address_components;
      angular.forEach( res, function(comp, idx){
        if(comp.types[0]=="postal_code"){
          $scope.currentProperty.zipcode = comp.long_name
        }
        if(comp.types[0]=="locality"){
          $scope.currentProperty.city = comp.long_name
        }
        if(comp.types[0]=="administrative_area_level_1"){
          $scope.currentProperty.state = comp.short_name
        }
      });
      $scope.currentProperty.latitude = parseFloat(data.results[0].geometry.location.lat);
      $scope.currentProperty.longitude = parseFloat(data.results[0].geometry.location.lng);
      $scope.currentProperty.fmt_address = data.results[0].formatted_address;
      $scope.currentProperty.street = $scope.currentProperty.fmt_address.split(",")[0];
      $scope.saveProperty();
      $scope.getGMapsURL();
    }).
      error(function(data){
      $scope.fadingAlert("address validation request failed");
    });
  };

  $scope.getGMapsURL = function(){
    var addr = $scope.currentProperty.street + " " + $scope.currentProperty.city + ", " + $scope.currentProperty.state;
    if ($scope.currentProperty.fmt_address){
      addr = $scope.currentProperty.fmt_address;
    }
    addr = encodeURIComponent( addr);
    var url = "https://www.google.com/maps/embed/v1/place?key=AIzaSyALGFTf_wfL3s_i-LrOJWS4wU1O4eRvMLE&q="
    url = url+addr;
    console.log(url);
    $scope.currentProperty.map_url = url;
  }

  $scope.openMap = function () {

    $scope.propertyMapModal = $modal.open({
      templateUrl: 'propertyMapModal.html',
      backdrop: true,
      size: 'sm',
      backdrop: true,
      windowClass: 'modal',
      controller: function ($scope, $modalInstance) {
        $scope.submit = function () {
          $modalInstance.dismiss('cancel');
        }
        $scope.cancel = function () {
          $modalInstance.dismiss('cancel');
        };
      }
    });
  };


  $scope.saveProperty = function( ){
    var putObj = {};
    putObj["street"] = $scope.currentProperty.street;
    putObj["city"] = $scope.currentProperty.city;
    putObj["state"] = $scope.currentProperty.state;
    putObj["zipcode"] = $scope.currentProperty.zipcode;
    //putObj["latitude"] = $scope.currentProperty.latitude;
    //putObj["longitude"] = $scope.currentProperty.longitude;
    return $scope.currentProperty.customPUT(putObj);
  }

  $scope.init();

});
