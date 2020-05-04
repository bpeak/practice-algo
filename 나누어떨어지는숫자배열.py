# pythonic solution to check empty list: https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty

def solution(arr, divisor):
  result = sorted(list(filter(lambda v: ( v % divisor ) == 0, arr)))
  return result if result else [-1]

print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3,2,6], 10))

def solution_better(arr, divisor):
  return sorted([v for v in arr if v % divisor == 0]) or [-1]

print(solution_better([5, 9, 7, 10], 5))
print(solution_better([2, 36, 1, 3], 1))
print(solution_better([3,2,6], 10))
