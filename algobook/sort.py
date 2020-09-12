def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]    
            else:
                break

def insertion_sort2(arr):
    for i in range(1, len(arr)):
        target_idx = i
        inserted_idx = target_idx
        for j in range(i - 1, 0 - 1, -1):
            if arr[j] > arr[target_idx]:
                inserted_idx = j
            else:
                break
        if target_idx != inserted_idx:
            arr[target_idx], arr[inserted_idx] = arr[inserted_idx], arr[target_idx]

arr = [1,5,3,6,7,4,2,4,5,2]
print(arr)
selection_sort(arr)
print(arr)

arr = [100,1,5,3,6,7,4,2,4,5,2]
print(arr)
insertion_sort(arr)
print(arr)

arr = [100,1,5,3,6,7,4,2,4,5,2]
print(arr)
insertion_sort2(arr)
print(arr)