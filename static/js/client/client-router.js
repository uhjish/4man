
'use strict';

angular.module('manpower')
.config(['$routeProvider', function ($routeProvider) {
  $routeProvider
  .when('/client/:clientId', {
    templateUrl: 'views/client/client-detail.html',
    controller: 'ClientController',
    resolve: {
      currentUser : function(User, $route){
        return User.get($route.current.params.client_id)
      }
    }
  });
}]);
