#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (const el of list) {
    if (el === searchElement) {
      i++;
    }
  }
  return i;
};
