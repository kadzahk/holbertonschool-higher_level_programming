#!/usr/bin/node
exports.converter = function (base) {
  function converterl (x) {
    return x.toString(base);
  }
  return converterl;
};
