from functools import cmp_to_key

def solution(n):
  def compare(a, b):
    if a > b:
      return -1
    else:
      return 1
  return int("".join([str(v) for v in sorted(map(int, str(n)), key=cmp_to_key(compare))]))

print(solution(118372))

# 한자리 숫자를 정렬하는건 숫자로 변환후 비교연산이 필요하지 않지 ( 당연 )
# 오름차순이면 1,2,3...
# 내림차순이면 3,2,1...
def solution2(n):
  return int("".join(sorted(list(str(n)), reverse=True)))

print(solution2(118372))
