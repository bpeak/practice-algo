def solution3(n):
    pass

"""
어린아이가 덧셈 하듯이
1씩 더했음
타임오버...
"""
def solution2(n):
    digits = [0]
    for i in range(n):
        digits[len(digits) - 1] += 1
        for j in range(len(digits) - 1, 0 - 1, -1):
            if digits[j] == 4:
                digits[j] = 1
                if j == 0:
                    digits.insert(0, 1)
                else:
                    digits[j - 1] += 1
    return "".join(["4" if digit == 3 else str(digit) for digit in digits])

# print(solution2(1))
# print(solution2(2))
# print(solution2(3))
# print(solution2(4))
# print(solution2(5))
# print(solution2(6))
# print(solution2(7))
# print(solution2(8))
# print(solution2(9))
# print(solution2(10))
# print(solution2(11))
# print(solution2(12))
# print(solution2(13))

"""
문제를 정확하게 이해 못했음
1
2
10
11
이 아니라
1
2
11
( 0 이없음 )
"""
def solution1(n):
    remains = []
    while(True):
        remain = n % 3
        quotient = n // 3
        n = quotient
        remains.append(str(remain))
        if quotient < 3:
            if quotient != 0:
                remains.append(str(quotient))    
            break        
    return "".join(reversed([digit for digit in remains]))

# print(solution1(1))
# print(solution1(2))
# print(solution1(3))
# print(solution1(4))
# print(solution1(5))
# print(solution1(6))



