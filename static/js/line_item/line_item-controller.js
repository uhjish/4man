
angular.module('manpower').
  controller("LineItemController",function(Restangular,$scope, $filter){

  $scope.init=function(li_id){
    Restangular.one('api/line_item', li_id).get().then( function (result){
      $scope.currentLineItem = result;
      $scope.getSubItems();
    });
  };

  $scope.subItems = [];
  $scope.getSubItems = function(){
    $scope.currentLineItem.getList('linesubitems').then(function(results){
      $scope.subItems = [];
      var costs = {'me':0.0,'le':0.0,'ma':0.0,'la':0.0};
      angular.forEach( results, function(si){
        si.costs = $scope.getSubItemCosts(si);
        costs.me += si.costs.me;
        costs.le += si.costs.le;
        costs.ma += si.costs.ma;
        costs.la += si.costs.la;
        $scope.subItems.push(si);
      });

      $scope.currentLineItem.costs = costs;
    });
  };

  $scope.getSubItemCosts = function(si){
    var costs = {'me':0.0,'le':0.0,'ma':0.0,'la':0.0};
    angular.forEach( si.subitemcosts, function( sic ){
      if (!sic.deleted_at){
        if (sic.is_estimate){
          costs.me += sic.material_cost;
          costs.le += sic.labor_cost;
        }else{
          costs.ma += sic.material_cost;
          costs.la += sic.labor_cost;
        }
      }
    });
    return costs;
  };
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
