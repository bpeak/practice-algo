function solution(numbers, target) {
  const candidateNumbers = []
  const find = (numbers, idx) => {
    const a = [...numbers]
    const b = [...numbers]
    b[idx] = -b[idx]
    if(numbers.length - 1 === idx) {
      candidateNumbers.push(b)
      candidateNumbers.push(a)
      return 
    }
    find(a, idx + 1)
    find(b, idx + 1)    
  }
  find(numbers, 0)
  return candidateNumbers.reduce((count, candidateNumber) => {
    const sum = candidateNumber.reduce((acc, curr) => acc + curr, 0)
    return count + Number(sum === target)
  }, 0)
}

console.log(solution([1,1,1,1,1], 3))