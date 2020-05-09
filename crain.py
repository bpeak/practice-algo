def solution(board, moves):
  basket = []
  score = 0
  for move in moves:
    idx = move - 1
    for row in board:
      if row[idx] == 0:
        continue
      basket.append(row[idx])
      row[idx] = 0
      break
    if len(basket) >= 2 and basket[len(basket) - 1] == basket[len(basket) - 2]:
      basket.pop()
      basket.pop()
      score += 2
  return score

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))