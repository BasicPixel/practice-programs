/*
https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/smallest-common-multiple
*/

function smallestCommons(arr) {
  const [min, max] = arr.sort((a, b) => a - b);

  let upperBound = 1;

  for (let i = min; i <= max; i++) {
    upperBound *= i;
  }

  for (let multiple = max; multiple <= upperBound; multiple += max) {
    let divisorCount = 0;
    for (let i = min; i <= max; i++) {
      if (multiple % i === 0) {
        divisorCount++;
      }
    }
    if (divisorCount === max - min + 1) {
      return multiple;
    }
  }
}

smallestCommons([1, 5]);
