function generateFibs(limit) {
  let fibs = [1, 1];

  let range = [...Array(limit - 1).keys()];

  for (let i = 1; i < range.length; i++) {
    fibs.push(fibs[i] + fibs[i - 1]);
  }
  return fibs;
}

function sumFibs(limit) {
  let fibs = generateFibs(limit);

  return fibs.reduce((a, b) => a + b);
}

function sumOddFibs(limit) {
  let fibs = generateFibs(limit);

  return fibs.filter((n) => n % 2 !== 0).reduce((a, b) => a + b);
}

console.log(sumFibs(10));
