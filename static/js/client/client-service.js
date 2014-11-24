'use strict';

angular.module('manpower')
  .factory('Client', ['$resource', function ($resource) {
    return $resource('manpower/notes/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
