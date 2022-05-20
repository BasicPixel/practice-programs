const greatestNum = (n: Array<number>) => {
  let greatest = n[0];

  n.forEach((number) => {
    if (number > greatest) greatest = number;
  });

  return greatest;
};

console.log(greatestNum([0]));
console.log(greatestNum([0, 1, 2, 3]));
console.log(greatestNum([4, 1.5, 222, 30]));
