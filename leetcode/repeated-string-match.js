const test = (A, B) => {
	let count = 1
	let A_next = A
	while(A_next.length < B.length) {
		A_next = A_next + A
		count++
    }
	if(A_next.includes(B)) {
		return count
	}
	if((A_next + A).includes(B)) {
		return count + 1
	}
	if((A + A_next).includes(B)) {
		return count + 1
	}
	if((A + A_next + A).includes(B)) {
		return count + 2
	}
	return -1
}
console.log(test("abcd" ,"cdabcdab")) // 3 3 2 5 4 2 -1
console.log(test("abcd", "cdabcdab"))
console.log(test("a", "aa"))
console.log(test("zbdb", "bzbdbzbdbzbdbzb"))
console.log(test("bb", "bbbbbbb"))
console.log(test("abccb", "cbabccb"))
console.log(test("abc", "aabcbabcc"))

/* 삽질 
const test = (A, B) => {
  let count = 0
  if(A.includes(B)) { return 1}
  const B_cleared = B.replace(new RegExp(A, "g"), function() {
      count++
      return ""
  })
  // console.log(count, B_cleared)
  if(B_cleared === "") { return count }
  const first_char = A[0]
  const idx = []
  for(let i = 0; i < B_cleared.length; i++) {
      if(B_cleared[i] === first_char) {
          idx.push(i)
      }
  }
  let flag = false
  if(B_cleared.length === 1) {
      if(A.includes(B_cleared)) {
          return count + 1
      }
  }
  console.log(B_cleared)
  if(A.startsWith(B_cleared) || A.endsWith(B_cleared)) {
      return count + 1
  }
  for(let i = 1; i < B_cleared.length; i++) {
      const start = B_cleared.slice(0, i)
      const end = B_cleared.slice(i, B_cleared.length)
      if(A.endsWith(start) && A.startsWith(end)) {
          flag = true
          break
      }
  }
  if(flag) {
      return count + 2
  } else {
      return -1
  }
}
*/