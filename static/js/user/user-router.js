'use strict';

angular.module('manpower')
.config(['$routeProvider', function ($routeProvider) {
  $routeProvider
  .when('/app/users', {
    templateUrl: 'views/user/users.html',
    controller: 'UserController',
    resolve:{
      resolvedUser: ['User', function (User) {
        return User.query();
      }]
    }
  })
}]);
