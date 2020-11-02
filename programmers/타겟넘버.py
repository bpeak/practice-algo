from collections import deque

def solution(numbers, target):
    firstNumber = numbers[0]
    candidates = [[firstNumber], [-firstNumber]]

    for number in numbers[1:]:
        next_candidates = []
        for candidate in candidates:
            candidate1 = candidate[:]
            candidate2 = candidate[:]
            candidate1.append(number)
            candidate2.append(-number)
            next_candidates.append(candidate1)
            next_candidates.append(candidate2)
        candidates = next_candidates
    
    result = 0
    for candidate in candidates:
        if sum(candidate) == target:
            result += 1
    return result

print(solution([1,2,3,4,5],3))