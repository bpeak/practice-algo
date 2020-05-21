class Solution:
    def freqAlphabets(self, s):
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        _map = {
            
        }
        for i in range(len(alphabets)):
            _map[str(i + 1)] = alphabets[i]
        
        result = ""
        
        skip = False
        skipCount = 0
        for i in range(len(s)):
            if skip:
                skipCount += 1
                if skipCount > 1:
                    skipCount = 0
                    skip = False
                continue
            if ((i + 2) <= len(s) - 1) and s[i+2] == "#":
                result += _map[s[i] + s[i + 1]]
                skip = True
            else:
                result += _map[s[i]]
        
        return result
            

s = Solution()
print(s.freqAlphabets("10#11#12"))