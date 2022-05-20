function range(start: number, end: number) {
  // https://stackoverflow.com/a/19506234/14900882
  return Array.apply(0, Array(end - 1)).map(
    (_element: any, index: number) => index + start
  );
}

function asciiTable(start: number, end: number) {
  if (end < start) {
    throw new Error("Ending number cannot be smaller than starting number.");
  }

  console.log("DEC\t\tHEX\t\tBIN\t\tCHAR");

  for (let i in range(start, end)) {
    console.log(`${i}\t\t${String.fromCharCode(parseInt(i))}`);
  }
}

asciiTable(1, 3);
asciiTable(3, 1);
