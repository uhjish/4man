angular.module('manpower').
  controller("ProjectController",function(Restangular,$scope, $filter, $http){
  var resource = Restangular.all('api/project')
  resource.getList().then(function(projects){
    $scope.projects = projects;
    $scope.edit(projects[0]);
    $scope.editMode = false;
  });
  
  $scope.statuses = [];
  Restangular.all('api/project_status').getList().then(function(sts){
    $scope.statuses = sts;
  });

  $scope.showStatus = function() {
      if($scope.statuses.length > 0) {
            var selected = $filter('filter')($scope.statuses, {id: $scope.currentProject.status_id});
            return selected.length  ? selected[0].status : 'Not set';
          } else {
                return "undefined"; //$scope.currentProject.status.status;
          }
    };
  $scope.lineItems = [];
  $scope.getLineItemsForProject = function(){
    $scope.currentProject.getList('line_items').then(function(results){
      $scope.lineItems = results;
    });
  };
  $scope.edit = function(selProj){
      $scope.currentProject = selProj;
      $scope.getLineItemsForProject();
  };
  $scope.add = function() {
    resource.post($scope.newproject).then(function(newResource){
        $scope.projects.push(newResource);
    })
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
  $scope.alert = function( resp ){
    $scope.edit(resp);
    $scope.editMode = true;
  };
});
