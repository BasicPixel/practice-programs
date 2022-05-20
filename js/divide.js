function divide(a, b) {
  let quotient = 0;
  let remainder = a;

  if (b === 0) {
    return "cannot divide by zero!";
  }

  if (a < b) {
    return [0, a];
  }

  while (remainder >= b) {
    quotient++;
    remainder -= b;
  }

  return [quotient, remainder];
}

console.log(divide(8.5, 2));
console.log(divide(8, 4));
console.log(divide(2, 4));
console.log(divide(2, 0));
