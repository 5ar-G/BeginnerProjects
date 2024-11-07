var h1 = document.getElementById("myh1");
var age = window.prompt("what is your age?");

age < 18
  ? (h1.textContent = "You are too young for this site")
  : age >= 18 && age < 100
  ? (h1.textContent = "You can visit this site")
  : (h1.textContent = "You are too old for this site");
