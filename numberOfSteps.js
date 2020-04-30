function isEven(num) {
  return num % 2 === 0
}

function numberOfSteps (num, step = 0) {
  if(num === 0) { return step }
  return isEven(num) ? numberOfSteps(num / 2, ++step) : numberOfSteps(num - 1, ++step)
}

console.log(numberOfSteps(14))