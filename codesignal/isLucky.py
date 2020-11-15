from functools import reduce

def isLucky(n):
    s = str(n)
    mid = len(s) // 2
    a = s[:mid]
    b = s[mid:]
    return sum([int(c) for c in a]) == sum([int(c) for c in b])
    # return reduce(lambda a, b: a + b, map(int, a)) == reduce(lambda a, b: a + b, map(int, b))

print(isLucky(1230))
print(isLucky(239017))

"""
기준 변수명 pivot
reduce
"""