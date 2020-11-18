def arrayChange(arr):
    result = 0
    for i in range(1, len(arr)):
        if arr[i - 1] >= arr[i]:
            v = arr[i - 1] - arr[i] + 1
            arr[i] += v
            result += v
    return result

print(arrayChange([1,1,1])) # 3
print(arrayChange([2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15])) # 13