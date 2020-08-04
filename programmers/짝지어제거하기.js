function solution(s) {
    const stack = []
    stack.push(s[0])
    for(let i = 1; i < s.length; i++) {
        const lastChar = stack[stack.length - 1]
        const currChar = s[i]
        if(lastChar === currChar) {
            stack.pop()
        } else {
            stack.push(currChar)
        }
    }
    return stack.length === 0 ? 1 : 0
}

console.log(solution('baabaa'))
console.log(solution('cdcd'))