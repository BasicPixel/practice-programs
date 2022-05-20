const digitCount = (n: number) => n.toFixed().length;

console.log(digitCount(8));
console.log(digitCount(800));
console.log(digitCount(80000));
console.log(digitCount(80.0));
console.log(digitCount(80.2131));
