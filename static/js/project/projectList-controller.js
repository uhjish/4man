angular.module('manpower').
  controller("ProjectListController",function($q, Restangular,$scope, $filter, $http, $location){

  var resource = Restangular.all('api/project')
  resource.getList().then(function(projects){
    $scope.projects = projects;
  });

  $scope.viewProject = function( project_id ){
    console.log("project:" + project_id);
    $location.path( 'project/' + project_id )
  }

});
