
angular.module('manpower').
  controller("LineItemListController",function($q, Restangular,$scope, $filter, lineItemPriceService){

  $scope.init=function(){
    $scope.getCurrentProject()
    .then(function(currentProject){

      $scope.project_id = currentProject.id;
      console.log(JSON.stringify(currentProject));

      currentProject.getList('line_items')
      .then(function( lItems ){
        $scope.lineItems = lItems;
      });

    });
    $scope.getPhases();
    $scope.getAreas();
    $scope.getCategories();
  };

  $scope.phases=[];
  $scope.getPhases = function(){
    Restangular.all('api/phase').getList()
    .then( function( res ){
      $scope.phases = res;

      console.log("PHASES!");
      console.log(JSON.stringify(res));
    });
  }

  $scope.areas=[];
  $scope.getAreas = function(){
    Restangular.all('api/area').getList()
    .then( function( res ){
      $scope.areas = res;
    });
  }
  $scope.categories=[];
  $scope.getCategories = function(){
    Restangular.all('api/category').getList()
    .then( function( res ){
      $scope.categories = res;
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

  $scope.updateLineItemTitle = function(newTitle, idx){
    var li = $scope.lineItems[idx];
    Restangular.one('api/line_item', li.id).customPUT({'title': newTitle})
    .then( function( res){
        $scope.lineItems[idx] = res;
        $scope.lineItems[idx].open = true;
    });
  }
  $scope.updateLineItemDesc = function(newDesc, idx){
    var li = $scope.lineItems[idx];
    Restangular.one('api/line_item', li.id).customPUT({'desc': newDesc})
    .then( function( res){
        $scope.lineItems[idx] = res;
        $scope.lineItems[idx].open = true;
    });
  }

  $scope.updateLineItemTrait = function(idx, trait, newtrait){
    var li = $scope.lineItems[idx];
    console.log(JSON.stringify(newtrait));
    var putObj = {};
    putObj[trait] = newtrait;
    Restangular.one('api/line_item', li.id).customPUT(putObj)
    .then( function( res){
        $scope.lineItems[idx] = res;
        $scope.lineItems[idx].open = true;
    });
  }

  $scope.deleteLineItem = function( idx ){
    var del_id = $scope.lineItems[idx].id;
    Restangular.one('api/line_item',del_id ).remove()
    .then( function(res){
        $scope.lineItems.splice(idx,1);
        lineItemPriceService.deleteLineItem( del_id );
    });
  }

  $scope.getLineItemCosts = function( li_id, cost_type ){
     var c =lineItemPriceService.getLineItemCosts(li_id);
     if (c) {
       if (c[cost_type]){
        return c[cost_type].toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
       }
     }
    return "(unk)";
  }

  $scope.closeAll = function(){
    $scope.lineItems.forEach( function( elem ){
      elem.open = false;
    });
  }

  $scope.addLineItem = function(){
    var postObj = {};
    postObj["title"]= "enter line item title";
    postObj["desc"]="enter line item description";
    postObj["project_id"] = $scope.project_id; 
    Restangular.all('api/line_item').post(postObj)
    .then( function(newLI){
        $scope.closeAll();
        newLI.open=true;
        $scope.lineItems.push(newLI);
    });
  }

});
