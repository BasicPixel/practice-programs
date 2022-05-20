const START = 1;
const LENGTH = 35;

let list = [];

console.log(`Start: ${START}, Limit: ${LENGTH}`);

for (let i = START; i <= LENGTH; i++) {
  list[i] = "";

  if (i % 3 === 0) list[i] += "Fizz";
  if (i % 5 === 0) list[i] += "Buzz";
  if (i % 3 !== 0 && i % 5 !== 0) list[i] += `${i}`;
}

for (let i = START; i < list.length; i++) {
  process.stdout.write(`${list[i]}, `);
}

console.log("\n");
