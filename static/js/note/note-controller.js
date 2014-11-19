'use strict';

angular.module('manpower')
  .controller('NoteController', ['$scope', '$modal', 'resolvedNote', 'Note',
    function ($scope, $modal, resolvedNote, Note) {

      $scope.notes = resolvedNote;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.note = Note.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Note.delete({id: id},
          function () {
            $scope.notes = Note.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Note.update({id: id}, $scope.note,
            function () {
              $scope.notes = Note.query();
              $scope.clear();
            });
        } else {
          Note.save($scope.note,
            function () {
              $scope.notes = Note.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.note = {
          
          "text": "",
          
          "created_at": "",
          
          "user_id": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var noteSave = $modal.open({
          templateUrl: 'note-save.html',
          controller: 'NoteSaveController',
          resolve: {
            note: function () {
              return $scope.note;
            }
          }
        });

        noteSave.result.then(function (entity) {
          $scope.note = entity;
          $scope.save(id);
        });
      };
    }])
  .controller('NoteSaveController', ['$scope', '$modalInstance', 'note',
    function ($scope, $modalInstance, note) {
      $scope.note = note;

      
      $scope.created_atDateOptions = {
        dateFormat: 'yy-mm-dd',
        
        
      };

      $scope.ok = function () {
        $modalInstance.close($scope.note);
      };

      $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
      };
    }]);
