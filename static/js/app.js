// Declare app level module which depends on filters, and services
var app = angular.module('manpower', ['ngResource', 'ngRoute', 'restangular','ui.bootstrap', 'ui.date', 'ngCookies', 'xeditable', 'uuid4', 'ngScrollSpy', 'bootstrapLightbox', 'angularFileUpload', 'wu.masonry'])
  .config(function ($routeProvider, RestangularProvider) {
    $routeProvider
      .when('/app', {
        templateUrl: 'views/home/home.html', 
        controller: 'HomeController'})
      .otherwise({redirectTo: '/app/'});

    // configure restangular
    //RestangularProvider.setBaseUrl('/api');

    // configure the response extractor for each request
    RestangularProvider.setResponseExtractor(function(response, operation) {
      // This is a get for a list
      var newResponse;
      if (operation === 'getList') {
        // Return the result objects as an array and attach the metadata
        newResponse = response.objects;
        newResponse.metadata = {
          numResults: response.num_results,
          page: response.page,
          totalPages: response.total_pages
        };
      } else {
        // This is an element
        newResponse = response;
      }
      return newResponse;
    });
});
app.factory('$modalogin', ['$rootScope', '$modal', '$http', '$cookieStore', '$q', function ($scope, $modal, $http, $cookie, $q) {
    
    return {
        login : function () {

            var deferred = $q.defer();
            
            if ($cookie.get('token')) {
                deferred.resolve($cookie.get('token'));
                return deferred.promise;
            }          

            var scope = $scope.$new(false);
            
            var modal = $modal.open({
                templateUrl: '/static/templates/modal_auth.html',
                scope: scope,
                keyboard: false,
            });

            scope.auth = {};
            scope.error = '';

            scope.do_auth = function () {
                $http({
                    url: '/api/v1/auth',
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    data: scope.auth,
                }).success(function(data, status) {
                    $cookie.put('token', data.token);
                    modal.close();
                    deferred.resolve(data.token);
                }).error(function(data, status) {
                    scope.error = data.description;
                });

            };
            
            return deferred.promise;
        }
    };

}]);

app.run(function(editableOptions, editableThemes) {
  editableOptions.theme = 'bs3';
  editableThemes.bs3.inputClass = 'input-sm';
  editableThemes.bs3.buttonsClass = 'btn-sm';
});

// --------------- Confirmation ----------------------
app.directive('ngConfirmClick', [
function(){
  return {
    link: function (scope, element, attr) {
      var msg = attr.ngConfirmClick || "Are you sure?";
      var clickAction = attr.confirmedClick;
      element.bind('click',function (event) {
        if ( window.confirm(msg) ) {
          scope.$apply(clickAction)
        }
      });
    }
  };
}]);
