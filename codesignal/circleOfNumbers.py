def circleOfNumbers(n, f):
    return [v for v in range(n)][int((f + n/2) % 10)]

# return ((n//2) + firstNumber) % n
print(circleOfNumbers(10, 2))
print(circleOfNumbers(6, 3))