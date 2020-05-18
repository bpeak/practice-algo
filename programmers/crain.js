function solution(board, moves) {
  let answer = 0;
  const basket = [];
  moves.forEach(move => {
    const col = move - 1
    for(let row = 0; row < board.length; row++) {
      if(board[row][col]) {
        basket.push(board[row][col])
        board[row][col] = 0
        break
      }
    }
    if(
      basket.length >= 2 &&
      basket[basket.length - 1] === basket[basket.length - 2]
    ) {
      answer += 2
      basket.pop()
      basket.pop()
    }
  })
  return answer;
}

const board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
const moves = [1,5,3,5,1,2,1,4]

console.log(solution(board, moves))
