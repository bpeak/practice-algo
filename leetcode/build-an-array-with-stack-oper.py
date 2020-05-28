class Solution:
    def buildArray(self, target, n):
        if len(target) == 0:
            return []
        result = [1]
        stack = ["Push"]
        if target == result:
            return stack
        for i in range(2, n + 1):
            if result[len(result) - 1] not in target:
                result.pop()
                stack.append("Pop")
            stack.append("Push")
            result.append(i)                            
            if target == result:
                return stack

s = Solution()
print(s.buildArray([1,3],3))
print(s.buildArray([2, 3, 4],4))