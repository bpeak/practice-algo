def solution(arr):
    count = 0
    i = 0
    while i < len(arr) - 1:
        # 순서O continue
        if arr[i] < arr[i + 1]:
            i += 1
            continue

        # 순서X
        if count >= 1:
            return False

        # 맨앞
        if i == 0:
            i += 1
            count += 1
            continue

        # 맨뒤
        if (i + 1) == len(arr) - 1:
            return True

        # arr[i] 를 뺀경우
        # [i - 1] - [i] - [i + 1]
        if arr[i - 1] < arr[i + 1]:
            i += 1
            count += 1
            continue
        # arr[i+1] 를 뺀경우
        # [i] - [i+1] - [i + 2]
        if arr[i] < arr[i + 2]:
            i += 2
            count += 1         
            continue
        return False
    return True    

print(solution([1, 3, 2, 1])) # false
print(solution([1, 3, 2])) # true
print(solution([1, 2, 1, 2])) # false
print(solution([10, 1, 2, 3, 4, 5]))  # true
print(solution([0, -2, 5, 6])) # true
print(solution([1, 1, 1, 2, 3])) # false