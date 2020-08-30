# 대칭 이용
class Solution:
    def reverseString(self, s):
        mid = len(s) / 2
        left = 0
        while left < mid:
            right = len(s) - 1 - left
            s[right], s[left] = s[left], s[right]
            left = left + 1

solution = Solution()
s = ["h","e","l","l","o"]
solution.reverseString(s)
print(s)

# two pointer
class Solution2:
    def reverseString(self, s):
        start = 0
        end = len(s) - 1
        while start < end:
            s[end], s[start] = s[start], s[end]
            start += 1
            end -= 1

solution2 = Solution2()
s = ["h","e","l","l","o"]
solution2.reverseString(s)
print(s)

class Solution3:
    def reverseString(self, s):
        s.reverse()

solution3 = Solution3()
s = ["h","e","l","l","o"]
solution3.reverseString(s)
print(s)