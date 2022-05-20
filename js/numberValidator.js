/* https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/javascript-algorithms-and-data-structures-projects/telephone-number-validator */

/* Test Cases
555-555-5555
(555)555-5555
(555) 555-5555
555 555 5555
5555555555
1 555 555 5555
*/

// Telephone Number Validator

function telephoneCheck(str) {
  // https://regex101.com for explanation
  const telephoneRegex = /^(1\s?)?(\d{3}|\(\d{3}\))[\s\-]?\d{3}[\s\-]?\d{4}$/gm;

  return telephoneRegex.test(str);
}

telephoneCheck('1 (555) 555-5555');
