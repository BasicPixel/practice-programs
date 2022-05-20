// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/sorted-union

function uniteUnique() {
  let args = [...arguments];
  let uniqueValues = [];

  for (let i in args) {
    for (let j in args[i]) {
      if (!uniqueValues.includes(args[i][j])) {
        uniqueValues.push(args[i][j]);
      }
    }
  }

  return uniqueValues;
}

uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]);
