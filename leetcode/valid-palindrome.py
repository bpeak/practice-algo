from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [c.lower() for c in s if c.isalnum()]
        chars = deque(chars)
        while len(chars) > 1:
            s = chars.popleft()
            e = chars.pop()
            if s != e:
                return False
        return True

class Solution2:
    def isPalindrome(self, s):
        chars = [c.lower() for c in s if c.isalnum()]
        return chars == chars[::-1]