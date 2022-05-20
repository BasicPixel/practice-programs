/* Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

https://codingbat.com/prob/p108886
*/

function sum67(nums: Array<number>) {
  let filtered: Array<number> = nums;

  // Filter the array
  if (nums.includes(6)) {
    let first = nums.slice(0, nums.indexOf(6));
    let second = nums.slice(nums.indexOf(7) + 1, nums.length);

    filtered = first.concat(second);
  }

  // Return the sum
  return filtered.reduce((acc, val) => acc + val, 0);
}

console.log(sum67([1, 2, 2]));
console.log(sum67([1, 2, 2, 6, 99, 99, 7]));
console.log(sum67([1, 1, 6, 7, 2]));
