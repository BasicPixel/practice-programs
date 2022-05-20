// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/missing-letters

/* Find the missing letter in the passed letter range and return it.
If all letters are present in the range, return undefined. */

function fearNotLetter(str) {
  let letters = "abcdefghijklmnopqrstuvwxyz";

  letters = letters.slice(
    letters.indexOf(str[0]),
    letters.indexOf(str[0]) + str.length
  );

  for (let i = 0; i < letters.length; i++) {
    if (str[i] !== letters[i]) {
      return letters[i];
    }
  }
  return undefined;
}

fearNotLetter("stvwx");
