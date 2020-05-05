def solution(p):
  return "*" * (len(p) - 4) + p[len(p) - 4 : len(p)]

print(solution("01033334444"))

# cf>
a = [1,2,3,4,5,6,7,8,9,10]
print(a[-4:])