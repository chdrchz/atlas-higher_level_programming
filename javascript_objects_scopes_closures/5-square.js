#!/usr/bin/node
import Rectangle from './4-rectangle';

class Square extends Rectangle {
  // initialization method
  constructor(size) {
    super(size, size);
  }
}
export default Square;
