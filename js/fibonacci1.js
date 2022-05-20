// Incomplete

function generateFibs(limit) {
  let fibs = [1, 1];

  let i = 1;

  while (1) {
    if (fibs[-1] >= limit) {
      break;
    } else {
      fibs.push(fibs[i] + fibs[i - 1]);
      i++;
    }
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

console.log(generateFibs(10));
