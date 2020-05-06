def solution(s):
  pCount = 0
  yCount = 0
  for c in s:
    c = c.lower()
    if c == 'p':
      pCount += 1
      continue
    if c == 'y':
      yCount +=1
      continue
  return True if pCount == yCount else False

print(solution("pPoooyY"))
print(solution("Pyy"))

def solution2(s):
  return s.lower().count('p') == s.lower().count('y')

print(solution2("pPoooyY"))
print(solution2("Pyy"))