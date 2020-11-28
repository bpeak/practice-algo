from collections import Counter

def palindromeRearranging(s):
    return len([v for v in Counter(s).values() if v % 2 != 0]) <= 1

print(palindromeRearranging("aabbccz"))  # True