let display = document.getElementById('display');

function appendValue(val) {
  display.value += val;
}

function clearDisplay() {
  display.value = '';
}

function calculate() {
  try {
    display.value = eval(display.value);
  } catch (err) {
    display.value = 'Error';
  }
}

// Bonus: Keyboard support (Optional for interns)
document.addEventListener("keydown", function (e) {
  if (!isNaN(e.key) || "+-*/.".includes(e.key)) {
    appendValue(e.key);
  } else if (e.key === "Enter") {
    calculate();
  } else if (e.key === "Backspace") {
    display.value = display.value.slice(0, -1);
  } else if (e.key === "Escape") {
    clearDisplay();
  }
});