#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  let k = 0;
  for (let i = (list.length - 1); i >= 0; i--) {
    revList[k] = list[i];
    k++;
  }
  return revList;
};
