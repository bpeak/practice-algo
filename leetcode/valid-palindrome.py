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