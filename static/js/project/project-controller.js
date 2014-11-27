angular.module('manpower').
  controller("ProjectController",function($q, Restangular,$scope, $filter, $http, $routeParams, $anchorScroll, $location){

  $scope.statuses = [];
  $scope.init = function(){
    $scope.project_id = $routeParams.id;
    console.log("project_id: " + $scope.project_id );
    Restangular.one('api/project', $scope.project_id).get()
    .then( function(result){
      $scope.currentProject = result;
      return $scope.currentProject.getList('line_items');
    })

    Restangular.all('api/project_status').getList().then(function(sts){
      $scope.statuses = sts;
    });

  }

  $scope.showProjectStatus = function() {
    if($scope.statuses.length > 0) {
      var selected = $filter('filter')($scope.statuses, {id: $scope.currentProject.status_id});
      return selected.length  ? selected[0].status : 'Not set';
    } else {
      return "undefined"; //$scope.currentProject.status.status;
    }
  };

  //update the fields on the backend
  $scope.saveProject = function() {
    var putObj = { "shortname": $scope.currentProject.shortname, 
      "desc" : $scope.currentProject.desc,
      "status_id" : $scope.currentProject.status_id
    };
    return $scope.currentProject.customPUT(putObj)
  };

  $scope.gotoAnchor = function(x) {
    var newHash = 'anchor' + x;
    if ($location.hash() !== newHash) {
      // set the $location.hash to `newHash` and
      // $anchorScroll will automatically scroll to it
      $location.hash('anchor' + x);
    } else {
      // call $anchorScroll() explicitly,
      // since $location.hash hasn't changed
      $anchorScroll();
    }
  };



  $scope.init();

});
