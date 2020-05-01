print([x * 10 for x in range(10)])

def solution(x, n):
  answer = [x * i for i in range(i, n + 1)]
  return answer

print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))