#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      let s = '';
      for (let k = 0; k < this.height; k++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
