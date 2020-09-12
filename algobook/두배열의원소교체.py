def solution(k, arr1, arr2):
    arr1.sort()
    arr2.sort(reverse=True)
    for i in range(k):
        if arr2[i] > arr1[i]:
            arr1[i] = arr2[i]
        else:
            break
    return sum(arr1)

print(solution(3, [1,2,5,4,3], [5,5,6,6,5]))