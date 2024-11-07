const min = 1;
const max = 100;
const answer = Math.floor(Math.random() * (max - min + 1) + min);

var attempts = 0;
var guess;
var running = true;
while (running) {
  guess = window.prompt("guess a number betwen " + min + " and " + max);
  guess = Number(guess);
  if (isNaN(guess)) {
    window.alert("please enter a valid number");
  } else if (guess < min || guess > max) {
    window.alert("please enter a valid number");
  } else {
    attempts++;
    if (guess < answer) {
      window.alert("too low");
    } else if (guess > answer) {
      window.alert("too high");
    } else {
      window.alert("correct");
      window.alert("It took you " + attempts + " attempts");
      running = false;
    }
  }
}
