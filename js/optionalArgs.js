/* https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/arguments-optional */

const addTogether = () => {
  const args = Object.values(arguments);

  if (args.map((arg) => arg).every((n) => typeof n === 'number')) {
    if (args.length === 1) {
      return function (b) {
        if (typeof b !== 'number') {
          return undefined;
        }
        return args[0] + b;
      };
    } else {
      return args[0] + args[1];
    }
  }

  return undefined;
};

addTogether(2, 3);

/* EXTRA SOLUTION

const addTogether = () => {
  const [first, second] = arguments;
  if (typeof(first) !== "number")
    return undefined;
  if (second === undefined)
    return (second) => addTogether(first, second);
  if (typeof(second) !== "number")
    return undefined;
  return first + second;
}

*/
