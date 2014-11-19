'use strict';

angular.module('manpower')
  .factory('User', ['$resource', function ($resource) {
    return $resource('manpower/users/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
