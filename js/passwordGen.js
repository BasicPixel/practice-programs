// passGen.js
// CLI Program that generates random passwords

const options = {
  length: 8,
  uppercase: true,
  lowercase: true,
  digits: true,
  symbols: true,
};

const chars = {
  uppercase: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
  lowercase: "abcdefghijklmnopqrstuvwxyz",
  digits: "0123456789",
  symbols: "!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~",
};

function generate() {
  let includedChars = "";

  // If no options are truthy, return with an error
  if (Object.values(options).every((val) => val != true)) {
    return "None of the options are true.";
  }

  // For each option, if it is truthy, add the corresponding characters to the included chars string
  Object.keys(options).forEach((option) => {
    if (options[option] == true) {
      includedChars += chars[option];
    }
  });

  // Shuffle the included chars string
  const randomized = includedChars
    .split("")
    .sort(() => 0.5 - Math.random())
    .join("");

  // Get the first [options.length] characters from the randomized string
  return randomized.slice(0, options.length);
}

console.log(generate());
