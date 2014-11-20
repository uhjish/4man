'use strict';

angular.module('manpower')
  .factory('User', ['$resource', function ($resource) {
    return $resource('api/user/:id', {}, {
      'query': { method: 'GET', isArray: true, 
            transformResponse: function(data, headersGetter){
              var d = angular.fromJson( data );
              data = d.objects;
              return(data);
            }},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
