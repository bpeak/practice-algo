def allLongestStrings(arr):
    maxLen = 0
    result = []
    for s in arr:
        if len(s) > maxLen:
            maxLen = len(s)
            result = [s]
        elif len(s) == maxLen:
            result.append(s)
    return result

print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))