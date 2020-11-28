def depositProfit(deposit, rate, threshold):
    count = 0
    while True:
        deposit = deposit * (1 + rate * 0.01)
        count += 1
        if deposit > threshold:
            return count        

print(depositProfit(100, 20, 170))
print(depositProfit(100, 1, 101))