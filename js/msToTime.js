const millisecondsToTime = (ms) => {
  let seconds = ms / 1000;
  let minutes = parseInt(seconds / 60, 10);
  seconds = parseInt(seconds % 60);
  let hours = parseInt(minutes / 60, 10);

  minutes = minutes % 60;

  return `${minutes}:${seconds}`;
};

// Wait 2 secs then log the time
const testFunc = async () => {
  await new Promise((r) => setTimeout(r, 2000));
  console.log(millisecondsToTime(performance.now()));
};

testFunc();
console.log(millisecondsToTime(performance.now()));
