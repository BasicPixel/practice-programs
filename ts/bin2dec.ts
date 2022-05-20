/**
 * Binary to decimal converter function
 * @param binary The number binary value
 * @returns The decimal representation of the number
 */
const dec = (binary: string) => {
  const prepared = binary.split("").reverse();

  let product = 0;

  prepared.forEach((digit, index) => {
    if (digit === "1") product += Math.pow(2, index);
  });

  return product;
};

console.log(`Binary: ${"00000001"} | Decimal: ${dec("00000001")}`);
console.log(`Binary: ${"00001011"} | Decimal: ${dec("00001011")}`);
console.log(`Binary: ${"00001111"} | Decimal: ${dec("00001111")}`);
console.log(`Binary: ${"00111000"} | Decimal: ${dec("00111000")}`);
