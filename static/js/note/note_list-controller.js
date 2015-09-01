angular.module('manpower').
  controller("NoteController",function(Restangular,$scope, $filter, $q){

  $scope.init=function(currentProject){
    Restangular.one('getCurrentUser').get()
    .then( function(res){
      $scope.current_user = res;
      return $scope.getCurrentProject();
    })
    .then( function(currentProject) {
      $scope.notes = currentProject.notes;
      $scope.notes.sort(function(a,b){return a.created_at - b.created_at;});
      $scope.notes.forEach( function(note){
        note.msg = note.note + " (" + note.created_at.substring(0,16) + ")";
      });
    });
  };

  $scope.getCurrentProject = function() {
    var deferred = $q.defer();
    $scope.$watch('currentProject', function(val) {
      if (val){
        deferred.resolve(val);
        console.log("found "+ val.shortname);
      }
    });
    return deferred.promise;
  };
});

