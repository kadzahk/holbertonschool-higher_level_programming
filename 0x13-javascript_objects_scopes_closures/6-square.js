#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let myStr = '';
    for (let i = 0; i < this.width; i++) {
      if (c === undefined) {
        myStr += 'X';
      } else {
        myStr += c;
      }
    }
    for (let j = 0; j < this.height; j++) {
      console.log(myStr);
    }
  }
}
module.exports = Square;
