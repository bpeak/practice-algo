def stringsRearrangement(arr):
    print(arr)
    arr.sort()
    print(arr)
    prevStr = arr[0]
    for nextStr in arr[1:]:
        diff = 0
        for c1, c2 in zip(prevStr, nextStr):
            diff += c1 != c2
        if diff != 1:
            return False
        prevStr = nextStr
    return True

# def isDiffOneChar(s1, s2):
#     diff = 0
#     for c1, c2 in zip(s1, s2):
#         diff += c1 != c2
#     if diff != 1:
#         return False
#     return True

print(stringsRearrangement([
    "abc", 
    "abx", 
    "axx", 
    "abx",
    "abc"])) # True


# print(stringsRearrangement([
#     "abc", 
#     "bef", 
#     "bcc", 
#     "bec", 
#     "bbc", 
#     "bdc"
# ])) # True

# print(stringsRearrangement(["aba", "bbb", "bab"])) # False
# print(stringsRearrangement(["ab", "bb", "aa"])) # True