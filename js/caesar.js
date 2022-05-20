/* https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/javascript-algorithms-and-data-structures-projects/caesars-cipher */

// Caesars Cipher Program

const rot13 = (str) => {
  let cipheredArr = [];

  for (let i in str) {
    if (/^[a-z]$/i.test(str[i])) {
      let code = str.charCodeAt(i);

      if (code + 13 <= 90) {
        code += 13;
      } else {
        let added = 90 - code;
        code = 65 + (13 - added) - 1;
      }

      const newChar = String.fromCharCode(code);
      cipheredArr.push(newChar);
    } else {
      cipheredArr.push(str[i]);
    }
  }

  return cipheredArr.join('');
};

rot13('SERR PBQR PNZC');
