/* https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/javascript-algorithms-and-data-structures-projects/palindrome-checker */

const palindrome = (str) => {
  // Regex to check if a char is alphanumeric
  const alphaRegex = /^[a-z0-9]+$/i;

  // Converts str to lowercase, splits it, then filters it to only keep alphanumeric characters
  const filtered = str
    .toLowerCase()
    .split('')
    .filter((c) => c.match(alphaRegex));

  // Stores the reversed filtered string in another variable
  // Used the spread operator so only the elements get copied and reversed, and not the original array
  const reverse = [...filtered].reverse();

  //   If every element in the reversed array matches the one in the original array, return true, else return false
  if (reverse.every((c, index) => c === filtered[index])) {
    return true;
  }
  return false;
};

palindrome('eye');
