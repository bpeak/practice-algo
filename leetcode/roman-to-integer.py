class Solution:
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    def romanToInt(self, s):
        skip = False
        result = 0
        for i in range(len(s)):
            if(skip == True):
                skip = False
                continue
            if(i == len(s) - 1 or self.roman_dict[s[i]] >= self.roman_dict[s[i + 1]]):
                result += self.roman_dict[s[i]]
            else:
                result += (self.roman_dict[s[i + 1]] - self.roman_dict[s[i]])
                skip = True
        return result
            