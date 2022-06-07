const defaultResult = 0;
let currentResult = defaultResult;

// This is a comment!

function getUserNumberInput() {
  return parseInt(userInput.value)
}

function createAndWriteLog(operator, resultBeforeCalc, calcNumber) {
  const calcDescription = `${currentResult} ${operator} ${calcNumber}`;
  outputResult(currentResult, calcDescription);
}

function add() {
  const enteredNumber = getUserNumberInput();
  const initialResult = currentResult;
  currentResult += enteredNumber;
  // alert(++currentResult);
  createAndWriteLog("+", initialResult, enteredNumber)
}

function subtract() {
  const enteredNumber = getUserNumberInput();
  const initialResult = currentResult;
  // currentResult -= enteredNumber;
  currentResult;
  createAndWriteLog("-", initialResult, enteredNumber);
}

function multiply() {
  const enteredNumber = getUserNumberInput();
  const initialResult = currentResult;
  currentResult *= enteredNumber;
  createAndWriteLog('*', initialResult, enteredNumber);
}

function divide() {
  const enteredNumber = getUserNumberInput();
  const initialResult = currentResult;
  currentResult /= enteredNumber;
  createAndWriteLog('/', initialResult, enteredNumber);
}

addBtn.addEventListener('click', add);
subtractBtn.addEventListener('click', subtract);
multiplyBtn.addEventListener('click', multiply);
divideBtn.addEventListener('click', divide);

