from collections import Counter

arr = [1,15,2,10,5,6,8,4,3,0]

def count_sort(arr):
    max_v = max(arr)
    counter = [0] * (max_v + 1)
    for v in arr:
        counter[v] += 1

    result = []
    for i in range(len(counter)):
        for j in range(counter[i]):
            result.append(i)
    return result

print(arr)
print(count_sort(arr))