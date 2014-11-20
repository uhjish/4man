'use strict';

angular.module('manpower')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/projects', {
        templateUrl: 'views/project/project-list.html',
        controller: 'ProjectController'
      })
    }]);
