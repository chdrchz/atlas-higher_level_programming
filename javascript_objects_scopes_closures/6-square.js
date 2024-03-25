#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  // initialization method
  constructor (size) {
    super(size, size);
  }

  // print method that changes char printed from x to c
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}
module.exports = Square;
