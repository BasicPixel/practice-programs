let equation = [0];
let lastEquationElement = String(equation.at(-1));
const isOperator = (c) => String(c).match(/[+/*]/);

const updateDisplay = (variable = equation.join('')) => {
  const display = document.getElementById('display');
  display.value = variable;
};

const handleClick = (value) => {
  // If button clicked is an operator, and the last item in the equation is also an operator, return and do nothing
  if (isOperator(value) && isOperator(lastEquationElement)) {
    equation.pop();
  }

  // Handle period click
  // if (value === '.') {
  //   let lastOpIndex =
  //     [...equation]
  //       .reverse()
  //       .join('')
  //       .search(/[+\-/*]/) -
  //     1 +
  //     equation.length;

  //   if (lastOpIndex === -1) {
  //     lastOpIndex = 0;
  //   }

  //   let lastNumber = equation.slice(lastOpIndex).join('');

  //   console.log(lastNumber);
  // }

  if (equation.join('') === '0') {
    if (!isOperator(value) && value !== '.') {
      equation = [value];
    }
  } else {
    equation.push(value);
  }
  updateDisplay();
};

const clear = () => {
  equation = [0];
  updateDisplay();
};

const handleEquals = () => {
  if (isOperator(lastEquationElement)) {
    equation.pop();
  }

  let answer = eval(equation.join(''));

  equation = [answer];

  updateDisplay();
};

document.addEventListener('DOMContentLoaded', () => {
  // Get all buttons, converts the result to an array, filter out the AC and = buttons
  const btns = Array.from(document.querySelectorAll('button')).filter(
    (btn) => btn.id !== 'clear' && btn.id !== 'equals'
  );

  // Add unique click listeners to clear and equals buttons
  document.getElementById('equals').addEventListener('click', handleEquals);
  document.getElementById('clear').addEventListener('click', clear);

  // Add eventListeners to button to handle click
  btns.forEach((btn) =>
    btn.addEventListener('click', () => {
      handleClick(btn.innerHTML);
    })
  );

  updateDisplay();
});
