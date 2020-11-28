def alphabeticShift(s):
    return "".join(['a' if c == 'z' else chr(ord(c) + 1) for c in s])

print(alphabeticShift('abz'))