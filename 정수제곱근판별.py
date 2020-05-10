import math

# 시간초과 난 방법
def solution_fail(n):
  i = 1
  while True:
    if i * i == n and i * i <= 50000000000000 :
      return (i + 1) * (i + 1)
    i += 1

# math.pow 모듈 이용 제곱근 계산
def solution(n):
  sqrt = math.pow(n, 0.5)
  sqrt_floored = math.floor(sqrt)
  return (sqrt_floored + 1) * (sqrt_floored + 1) if sqrt - sqrt_floored == 0 else -1

# math.pow 없이 ( with % 1 ) **
def solution_(n):
  sqrt = n ** (0.5)
  if sqrt % 1 == 0:
    return (sqrt + 1) ** 2
  return -1