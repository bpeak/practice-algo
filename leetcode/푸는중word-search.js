let visited = {}
const exist = (board, word) => {
    const find = (i, j, charIdx) => {
        // top
        const targets = []
        if(i - 1 >= 0 && board[i - 1][j] === word[charIdx] && !visited[`${i - 1}-${j}`]){
            visited[`${i - 1}-${j}`] = true
            if(word[charIdx] === word[word.length - 1] && charIdx === word.length - 1) {
                return true
            } else {
                targets.push({
                    i: i - 1,
                    j: j,
                    charIdx: charIdx + 1
                })
                // return find(i - 1, j, charIdx + 1)
            }
        }
        // down
        if(i + 1 <= board.length - 1 && board[i + 1][j] === word[charIdx] && !visited[`${i + 1}-${j}`]) {
            visited[`${i + 1}-${j}`] = true
            if(word[charIdx] === word[word.length - 1] && charIdx === word.length - 1) {
                return true
            } else {
                targets.push({
                    i: i + 1,
                    j: j,
                    charIdx: charIdx + 1
                })
                // return find(i + 1, j, charIdx + 1)
            }
        }
        // left
        if(j - 1 >= 0 && board[i][j - 1] === word[charIdx] && !visited[`${i}-${j-1}`]) {
            visited[`${i}-${j-1}`] = true
            if(word[charIdx] === word[word.length - 1] && charIdx === word.length - 1) {
                return true
            } else {
                targets.push({
                    i: i,
                    j: j - 1,
                    charIdx: charIdx + 1
                })
                // return find(i, j - 1, charIdx + 1)
            }
        }
        // right
        if(j + 1 <= board[i].length - 1 && board[i][j + 1] === word[charIdx] && !visited[`${i}-${j+1}`]) {
            visited[`${i}-${j+1}`] = true
            // console.log(visited)
            if(word[charIdx] === word[word.length - 1] && charIdx === word.length - 1) {
                return true
            } else {
                targets.push({
                    i: i,
                    j: j + 1,
                    charIdx: charIdx + 1
                })
                // return find(i, j + 1, charIdx + 1)
            }
        }
        const results = targets.map(target => {
            visited[`${target.i}-${target.j}`] = true
            return find(target.i, target.j, target.charIdx)
        })
        for(let i = 0; i < results.length; i++) {
            if(results[i]) {
                return true
            }
        }
        return false
    }
    const targets = []
    for(let i = 0; i< board.length; i++) {
        for(let j = 0; j < board[i].length; j++) {
            if(board[i][j] === word[0]) {
                if(word.length === 1) {
                    return true
                }
                targets.push({
                    i: i,
                    j: j,
                    charIdx: 1,
                })
                // console.log(i, j, 1, word[1], "찾자")
                // return find(i, j, 1)
            }
        }
    }
    const results = targets.map(target => {
        visited = {}
        visited[`${target.i}-${target.j}`] = true
        return find(target.i, target.j, target.charIdx)
    })
    for(let i = 0; i < results.length; i++) {
        if(results[i]) {
            return true
        }
    }
    return false
};
console.log(exist([
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
  ], "ABCCED"))
  console.log(exist([
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
  ], "SEE"))
  console.log(exist([
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
  ], "ABCB"))
  console.log(exist([
    ['A']
  ], "A"))