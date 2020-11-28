def isIPv4Address(s):
    tokens = s.split(".")
    if len(tokens) != 4:
        return False
    return sum([1 for token in tokens if \
        token.isdigit() and \
        0 <= int(token) <= 255 and \
        len(str(int(token))) == len(token)]) == 4

print(isIPv4Address("3.3.3.3"))
print(isIPv4Address("3.3.3.333"))
print(isIPv4Address("3.3.3.00"))