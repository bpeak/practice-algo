def solution1(x):
  sumOfDigitNumber = 0
  for c in str(x):
    sumOfDigitNumber += int(c)
  return ( x % sumOfDigitNumber ) == 0

print(solution1(10))
print(solution1(12))
print(solution1(11))
print(solution1(13))

def solution2(x):
  return x % sum([int(c) for c in str(x)]) == 0

print(solution2(10))
print(solution2(12))
print(solution2(11))
print(solution2(13))