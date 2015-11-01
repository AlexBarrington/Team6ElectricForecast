/**
* Register controller
* @namespace thinkster.authentication.controllers
*/
(function () {
  'use strict';

  var app = angular.module('electricForcastApp.controllers', []);

  app.controller('LayoutController', ['$scope', '$http', 'CalculatorService', function($scope, $http, CalculatorService){

   console.log('in LayoutController...');
    $scope.openOpAreaPage = function() {
     window.location.href="{% url OpAreaView opAreaName %}";
   };

  }]);

  /**
  * @namespace RegisterController
  */
  function RegisterController($location, $scope, Authentication) {
    var vm = this;

    vm.openOpAreaPage = openOpAreaPage;

    /**
    * @name openOpAreaPage
    * @desc Opens an OpArea page based on the click
    */
    function openOpAreaPage(opAreaName) {
      /*insert method body here*/
      window.location.href="{% url OpAreaView opAreaName %}";
    }
  }
})();
