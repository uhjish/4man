angular.module('manpower').
  controller("ClientController",function($q, Restangular,$scope, $filter, $http, $modal, $routeParams){

  $scope.currentId = $routeParams.clientId;
  $scope.init=function(){
    if ($scope.currentId){
      $scope.parseDeps($scope.currentId);
    }else{
      $scope.getCurrentProject()
      .then(function(val){
        $scope.parseDeps(val.user_id);
      });
    }
    $scope.channels = $scope.getContactChannels();

  };
 
  $scope.getContactChannels = function(){
    return ["home-phone","office-phone","mobile-phone","email","other"];
  }
  $scope.getFormattedAddress = function(){
    var ct = $scope.currentContact;
    if (!ct){
      return "...loading...";
    }
    $scope.currentContact.address =  ct.street + "\n" + ct.city + ", " + ct.state + " " + ct.zipcode;
    return $scope.currentContact.address;
  } 

  $scope.parseDeps = function( client_id ){
    $scope.client_id = client_id;
    var deps =  Restangular.one('api/user', $scope.client_id).get()
    .then( function (result){
      $scope.currentUser = result;
      console.log(JSON.stringify(result));
      return Restangular.one('api/contact', $scope.currentUser.contact_id).get();
    })
    .then( function (r2){
      $scope.currentContact = r2;
      console.log(JSON.stringify(r2.items));
    });

    return deps;
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


  $scope.addContactItem = function(){
   // $scope.currentContact;
    var postObj = {};
    postObj["channel_id"]=1;
    postObj["contact_id"]= $scope.currentContact.id;
    postObj["label"]="default label";
    postObj["identifier"]="555-555-5555";
    Restangular.all('api/contact_item').post(postObj)
    .then( function(newObj){
      $scope.currentContact.items.push(newObj);
    });
  }

  $scope.saveContactItems = function(){
    angular.forEach( $scope.currentContact.items, function( item, idx){
      var putObj = { "label": item.label,
                      "identifier": item.identifier };
      Restangular.one('api/contact_item', item.id).customPUT(putObj);
    });
  }

  $scope.deleteContactItem = function(idx){
    del_id = $scope.currentContact.items[idx].id;
    Restangular.one('api/contact_item', del_id).remove()
    .then( function(result){
      $scope.currentContact.items.splice(idx,1);
    });
  }

  $scope.updateClientName = function( newname ){
    $scope.currentContact.fullname = newname;
    $scope.currentContact.customPUT( {"fullname": newname } );
  }

  $scope.updateClientLogin = function( newlogin ){
    $scope.currentUser.email = newlogin;
    $scope.currentUser.customPUT( {"email": newlogin } );
  }
  
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

  $scope.validateAddress = function( addr ){
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
          $scope.currentContact.zipcode = comp.long_name
        }
        if(comp.types[0]=="locality"){
          $scope.currentContact.city = comp.long_name
        }
        if(comp.types[0]=="administrative_area_level_1"){
          $scope.currentContact.state = comp.short_name
        }
      });
      $scope.currentContact.fmt_address = data.results[0].formatted_address;
      $scope.currentContact.street = $scope.currentContact.fmt_address.split(",")[0];
      $scope.currentContact.customPUT(
        { "street": $scope.currentContact.street,
          "city":   $scope.currentContact.city,
          "state":  $scope.currentContact.state,
          "zipcode":$scope.currentContact.zipcode}
      ).error(function(data){
        $scope.fadingAlert("failed to update address! "+ JSON.stringify(data))
      });
      
    }).
      error(function(data){
      $scope.fadingAlert("address validation request failed! " + JSON.stringify(data));
    });
  };

  $scope.init();

});
