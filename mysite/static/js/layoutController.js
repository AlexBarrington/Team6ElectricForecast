/**
* Register controller
* @namespace thinkster.authentication.controllers
*/
(function () {
  'use strict';

  var app = angular.module('electricForcastApp.controllers', []);

  app.controller('LayoutController', ['$scope', '$http', 'CalculatorService', function($scope, $http){

   console.log('in LayoutController...');
    $scope.openOpAreaPage = function(opAreaName) {
     window.location.href="{% url OpArea opAreaName %}";
   };

  }]);
})();
