#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    for (let i = 0; i < list.length; i++) {
      if (searchElement === list[i]) {
        let occurences;
        occurences += 1;
      }
      return occurences;
    }
}
