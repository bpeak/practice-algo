def solution(inp):
    n, k = map(int, inp.split())
    count = 0
    while n != 1:
        if n % k == 0:
            n = n // k
        else:
            n -= 1
        count += 1
    return count


print(solution("25 5"))