'use strict';

angular.module('manpower')
.factory('lineItemPriceService', [function($rootScope, $filter){
  
  var lineItemPrices = {};
  
  var updateLineItem = function( newLI ){
    lineItemPrices[ newLI.id ] = newLI.costs;
  }

  var deleteLineItem = function( li_id ){
    delete lineItemPrices[li_id];  
  }

  var getLineItemCosts = function( li_id ){
    return lineItemPrices[li_id];
  }

  var getTotalCosts = function(){
    costs = { "est_material": 0.0,
              "est_labor":    0.0,
              "act_material": 0.0,
              "act_labor":    0.0}
    for( var li_id in lineItemPrices ){
        c = lineItemPrices[li_id];
        costs.est_material += c.est_material;
        costs.est_labor += c.est_labor;
        costs.act_material += c.act_material;
        cost.act_labor += c.act_labor;
    }
    return costs;
  }

  return {
    updateLineItem:   updateLineItem,
    deleteLineItem:   deleteLineItem,
    getLineItemCosts: getLineItemCosts,
    getTotalCosts:    getTotalCosts
  };

}]);
