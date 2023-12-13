#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let re = '';
      for (let k = 0; k < this.width; k++) {
        re += 'X';
      }
      console.log(re);
    }
  }
}

module.exports = Rectangle;
