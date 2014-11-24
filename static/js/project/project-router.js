'use strict';

angular.module('manpower')
.config(['$routeProvider', function ($routeProvider) {
  $routeProvider
  .when('/projects', {
    templateUrl: 'views/project/project-list.html',
    controller: 'ProjectListController'
  })
  .when('/project/:id', {
    templateUrl: 'views/project/project.html',
    controller: 'ProjectController'
  })
}]);
