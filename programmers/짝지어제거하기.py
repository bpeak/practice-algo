def solution(string):
    stack = [string[0]]
    for i in range(1, len(string)):
        currChar = string[i]
        if len(stack) == 0:
            stack.append(currChar)
            continue
        prevChar = stack[-1]
        if prevChar == currChar:
            stack.pop()
        else:
            stack.append(currChar)
    if len(stack) == 0:
        return 1
    else:
        return 0

def solution2(string): #첫번째 요소도 일관성유지
    stack = []
    for i in range(len(string)):
        currChar = string[i]
        if len(stack) == 0:
            stack.append(currChar)
            continue
        prevChar = stack[-1]
        if prevChar == currChar:
            stack.pop()
        else:
            stack.append(currChar)
    if len(stack) == 0:
        return 1
    else:
        return 0        

print(solution2('baabaa'))
print(solution2('cdcd'))