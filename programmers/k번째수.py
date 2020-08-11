def solution(array, commands):
    answer = []
    for command in commands:
        startNum, endNum, k = command
        startIdx = startNum - 1
        endIdx = endNum - 1
        idx = k - 1
        v = sorted(array[startIdx:endIdx + 1])[idx]
        answer.append(v)
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

def solution_short(array, commands):
    answer = []
    for command in commands:
        answer.append(sorted(array[command[0] - 1:command[1]])[command[2] - 1])
    return answer