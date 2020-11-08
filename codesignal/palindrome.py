def checkPalindrome(inputString):
    start = 0
    end = len(inputString) - 1
    while start <= end:
        if inputString[start] != inputString[end]:
            return False
        start += 1
        end -= 1
    return True

print(checkPalindrome('aabaa'))
print(checkPalindrome('abac'))
print(checkPalindrome('a'))