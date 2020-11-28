def evenDigitsOnly(n):
    for v in str(n):
        if v % 2 != 0:
            return False
    return True

print(12345)
print('a'.isdigit())
print('1'.isalpha())