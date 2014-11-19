'use strict';

angular.module('manpower')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/notes', {
        templateUrl: 'views/note/notes.html',
        controller: 'NoteController',
        resolve:{
          resolvedNote: ['Note', function (Note) {
            return Note.query();
          }]
        }
      })
    }]);
