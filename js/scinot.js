// scinot.js
// Produces the scientific notation of a given number

const scinot = (n) => {
  let power = 0;

  while (n < 1) {
    n *= 10;
    power--;
  }

  while (n > 10) {
    n /= 10;
    power++;
  }

  return `${n} * 10^${power}`;
};
