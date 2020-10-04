def solution(v, count=0):
    if v == 1:
        return count
    count +=1
    candidates = []
    if v % 5 == 0:            
        candidates.append(solution(v // 5, count))
    elif v % 3 == 0:
        candidates.append(solution(v // 3, count))
    elif v % 2 == 0:
        candidates.append(solution(v // 2, count))
    candidates.append(solution(v - 1, count))
    return min(candidates)

print(solution(26))

def solution2(v, count):
    pass

print(solution(26))