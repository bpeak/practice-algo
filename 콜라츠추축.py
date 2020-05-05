def isEven(num):
  return True if num % 2 == 0 else False

def solution(num, steps=0):
  if num == 1:
    return steps
  if steps == 500:
    return -1
  return solution(num / 2, steps + 1) if isEven(num) else solution(num * 3 + 1, steps + 1)

print(solution(6))
print(solution(16))
print(solution(626331))

def solution2(num):
  for i in range(1, 500 + 1):
    num = num / 2 if num % 2 == 0 else num * 3 + 1
    if num == 1:
      return i
  return -1

print(solution2(6))
print(solution2(16))
print(solution2(626331))



