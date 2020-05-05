def solution(p):
  return "*" * (len(p) - 4) + p[len(p) - 4 : len(p)]

print(solution("01033334444"))