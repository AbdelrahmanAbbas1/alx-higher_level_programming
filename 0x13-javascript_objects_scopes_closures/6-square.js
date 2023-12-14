#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
