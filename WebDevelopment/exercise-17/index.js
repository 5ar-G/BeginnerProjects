var labell = document.getElementById("mylabel");
var button = document.getElementById("mybutton");
var number;
var min = 1;
var max = 100;

button.onclick = function () {
  number = Math.floor(Math.random() * max) + min;
  labell.textContent = number;
};
