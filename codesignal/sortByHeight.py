from collections import deque

def sortByHeight(arr):
    heights = deque(sorted([v for v in arr if v != -1]))
    result = []
    for v in arr:
        if v == -1:
            result.append(-1)
        else:
            result.append(heights.popleft())
    print(result)

print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))