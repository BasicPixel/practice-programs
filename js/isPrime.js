// Algorithm from https://stackoverflow.com/a/40200710/14900882

const isPrime = (n) => {
  for (var i = 2; i < n; i++) if (n % i === 0) return false;
  return n > 1;
};

const testPrime = (n) => {
  console.log(`${n}: `, isPrime(n));
};

let tests = [-4, -3, -1, 0, 1, 2, 4, 8, 13];

tests.forEach((n) => console.log(`${n}: ${isPrime(n)}`));
