/*
https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/binary-agents
*/

const binaryAgent = (str) => {
  let binary = str.split(' ');
  let unicode = [];

  for (let i in binary) {
    unicode.push(String.fromCharCode(parseInt(binary[i], 2)));
  }

  return unicode.join('');
};

binaryAgent(
  '01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111'
);
