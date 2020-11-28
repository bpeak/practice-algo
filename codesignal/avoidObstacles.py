def avoidObstacles(arr):
    m = max(arr)
    for k in range(2, m + 1):
        for v in arr:
            if v % k == 0:
                break
        else:
            return k
    return m + 1

print(avoidObstacles([5, 3, 6, 7, 9]))  # 4
print(avoidObstacles([2, 3]))  # 4

''' js
function avoidObstacles(arr) {
  for(var n=1;;n++) if(arr.every(x=>x%n)) return n
}
'''

# 1은 할필요 없음, var => let, end length