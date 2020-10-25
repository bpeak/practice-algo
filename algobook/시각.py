def solution(N):
    allCase = 3600
    containThreeCase = allCase - 45 * 45
    total = 0
    for i in range(N + 1):
        s = str(i)
        if '3' in s:
            total += allCase
        else:
            total += containThreeCase
    return total

print(solution(5))

def solution_brutal(N):
    total = 0
    for h in range(N + 1):
        for m in range(60):
            for s in range(60):
                hms = str(h) + str(m) + str(s)
                if '3' in hms:
                    total += 1
    return total                    

print(solution_brutal(5))