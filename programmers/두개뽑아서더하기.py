def solution(numbers):
    result = set()
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            result.add(numbers[i] + numbers[j])
    return sorted(list(result))

print(solution([2,1,3,4,1]))
