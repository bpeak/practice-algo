def solution(n, m, k, numbers):
    mainNumber, subNumber = list(reversed(sorted(numbers)))[0:2]
    isMainNumber = True
    result = 0
    count = 0
    for _ in range(m):
        v = mainNumber if isMainNumber else subNumber
        result += v
        count += 1
        if isMainNumber:
            if count != k:
                continue
            isMainNumber = False
            count = 0
        else:
            isMainNumber = True
    return result

print(solution(5, 8, 3, [2, 4, 5, 4, 6]))

def solution2(n, m, k, numbers):
    mainNumber, subNumber = list(reversed(sorted(numbers)))[0:2]
    count = ( m // ( k + 1 ) ) * k + m % ( k + 1 )
    result = mainNumber * count + subNumber * (m - count)
    return result

print(solution2(5, 8, 3, [2, 4, 5, 4, 6]))
