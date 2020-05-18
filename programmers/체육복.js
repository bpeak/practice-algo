const solution = (STUDENT_COUNT, lostedStudents, sparedStudents) => {
  n = STUDENT_COUNT - lostedStudents.length

  lostedStudents.sort()
  lostedStudents = new Set(lostedStudents)
  sparedStudents = new Set(sparedStudents)
  lentedStudents = new Set()

  for(let me of lostedStudents) {
    let front = me - 1
    let back = me + 1
    if(
      sparedStudents.has(front) &&
      !lostedStudents.has(front) &&
      !lentedStudents.has(front)
    ){
      lentedStudents.add(front)
      n++
      continue
    }
    if(
      sparedStudents.has(me) &&
      !lentedStudents.has(me)
    ){
      lentedStudents.add(me)
      n++
      continue
    }
    if(
      sparedStudents.has(back) &&
      !lostedStudents.has(back) &&
      !lentedStudents.has(back)
    ) {
      lentedStudents.add(back)
      n++
      continue
    }
  }

  return n
}

console.log(solution(5, [2,4], [1,3,5])) // 5
console.log(solution(5, [2,4], [3])) // 4
console.log(solution(3, [3], [1])) // 2