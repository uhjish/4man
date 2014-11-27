
angular.module('manpower').
  controller("LineItemController",function(Restangular,$scope, $filter, $q, lineItemPriceService){

  $scope.init=function(li_id){
    Restangular.one('api/line_item', li_id).get()
    .then( function(li){
      $scope.currentLineItem = li;
      $scope.getSubItems();
    });
  };

  $scope.getCurrentLineItem = function() {
    var deferred = $q.defer();
    $scope.$watch('li', function(val) {
      if (val){
        deferred.resolve(val);
        console.log("found "+ val.shortname);
      }
    });
    return deferred.promise;
  };

  $scope.subItems = [];
  $scope.getSubItems = function(){
    $scope.currentLineItem.getList('linesubitems')
    .then(function(results){
      $scope.subItems = results;
      $scope.updateTotalCosts();
    });
  };

  $scope.updateTotalCosts = function(){
      var costs = {'est_material':0.0,'est_labor':0.0,'act_material':0.0,'act_labor':0.0};
      angular.forEach( $scope.subItems, function(si){
        costs.est_material += si.est_material;
        costs.est_labor += si.est_labor;
        costs.act_material += si.act_material;
        costs.act_labor += si.act_labor;
      });
      $scope.currentLineItem.costs = costs;
      lineItemPriceService.updateLineItem( $scope.currentLineItem );
  }

  $scope.deleteSubitem = function(index){
    Restangular.one('api/line_subitem', $scope.subItems[index].id).remove();
    $scope.subItems.splice(index, 1);
    $scope.updateTotalCosts();
  }

  $scope.updateSubitem = function(data, idx){
    var si_id = $scope.subItems[idx].id;
    var putObj = {}
    putObj["desc"] = data.desc;
    putObj["est_material"] = data.est_material;
    putObj["est_labor"] = data.est_labor;
    putObj["act_material"] = data.act_material;
    putObj["act_labor"] = data.act_labor;
    Restangular.one('api/line_subitem', si_id).customPUT(putObj)
    .then(function(res){
      //rejoice
      $scope.subItems[idx] = res;
      $scope.updateTotalCosts();
    });
  }


  $scope.addSubitem = function(){
    var postObj = { desc: "enter subitem description",
                    lineitem_id: $scope.currentLineItem.id };
    Restangular.all('api/line_subitem').post(postObj).then( function( res ){
      console.log( JSON.stringify( res ));
      $scope.subItems.push( res );
    });
    $scope.updateTotalCosts();
  }
  $scope.saveProject = function() {
    // $scope.user already updated!
    return $http.post('/project', $scope.currentProject).error(function(err) {
      if(err.field && err.msg) {
        // err like {field: "name", msg: "Server-side error for this username!"} 
        $scope.editableForm.$setError(err.field, err.msg);
      } else { 
        // unknown error
        $scope.editableForm.$setError('name', 'Unknown error!');
      }
    });
  };
});
