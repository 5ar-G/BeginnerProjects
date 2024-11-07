const display = document.querySelector("input");
function appendOnDisplay(input) {
  display.value += input;
}
function cleaDisplay() {
  display.value = "";
}
function calculate() {
  try {
    display.value = eval(display.value);
  } catch (error) {
    display.value = "Error";
  }
}
