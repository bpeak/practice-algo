from itertools import permutations

def stringsRearrangement(arr):
    for ar in permutations(arr, len(arr)):
        prevStr = ar[0]
        for nextStr in ar[1:]:
            diff = 0
            for c1, c2 in zip(prevStr, nextStr):
                diff += c1 != c2
            if diff != 1:
                break
            prevStr = nextStr
        else:
            return True
    return False

print(stringsRearrangement([
    "abc", 
    "abx", 
    "axx", 
    "abx",
    "abc"])) # True

print(stringsRearrangement([
    "abc", 
    "bef", 
    "bcc", 
    "bec", 
    "bbc", 
    "bdc"
])) # True

print(stringsRearrangement(["aba", "bbb", "bab"])) # False
print(stringsRearrangement(["ab", "bb", "aa"])) # True    
