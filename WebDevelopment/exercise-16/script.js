var increaseButton = document.getElementById("increase");
var decreaseButton = document.getElementById("decrease");
var resetButton = document.getElementById("reset");
var myLabel = document.getElementById("mylabel");
var count = 0;

increaseButton.onclick = function () {
  count++;
  myLabel.textContent = count;
};
decreaseButton.onclick = function () {
  count--;
  myLabel.textContent = count;
};
resetButton.onclick = function () {
  count = 0;
  myLabel.textContent = count;
};
