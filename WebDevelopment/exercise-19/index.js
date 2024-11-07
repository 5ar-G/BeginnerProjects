var h1 = document.getElementById("myh1");
var h2 = "";
while (h2 === "") {
  h2 = window.prompt("what is your name");
}
h1.textContent = "hello " + h2 + " ,this is a red square";
