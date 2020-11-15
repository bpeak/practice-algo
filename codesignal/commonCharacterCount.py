from collections import Counter

def commonCharacterCount(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    if len(c1) >= len(c2):
        src = c1
        dest = c2
    else:
        src = c2
        dest = c1
    result = 0
    for k in src:
        result += min(src[k], dest[k])
    return result

print(commonCharacterCount("aabcc", "adcaa"))

# short
def commonCharacterCount2(s1, s2):
    return sum([min(s1.count(c), s2.count(c)) for c in set(s1)])

print(commonCharacterCount2("aabcc", "adcaa"))