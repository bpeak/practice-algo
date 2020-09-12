arr = [1,3,6,7,8,10,34,44,33,22,4,46,55,2,32,5]
arr.sort()

def sequential_search(arr, target):
    for i, v in enumerate(arr):
        # print('s')
        if target == v:
            return i
    else:
        return -1

def binary_search(arr, target, start=0, end=len(arr) - 1):
    # print('b')
    if start > end :
        return -1
    mid = ( start + end ) // 2
    if target == arr[mid]:
        return mid
    if target < arr[mid]:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)

def binary_search2(arr, target):
    start = 0
    end = len(arr) - 1

    while start < end:
        # print('b2')
        mid = ( start + end ) // 2
        if target == arr[mid]:
            return mid
        if target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


print(arr)
print(sequential_search(arr, 44))
print(binary_search(arr, 44))
print(binary_search2(arr, 44))
print(sequential_search(arr, 444))
print(binary_search(arr, 444))
print(binary_search2(arr, 444))