def solution(v, count=0):
    print(v, 'solution1')
    if v == 1:
        return count
    count +=1
    candidates = []
    if v % 5 == 0:            
        candidates.append(solution(v // 5, count))
    elif v % 3 == 0:
        candidates.append(solution(v // 3, count))
    elif v % 2 == 0:
        candidates.append(solution(v // 2, count))
    candidates.append(solution(v - 1, count))
    return min(candidates)

print(solution(26))

# def solution2(v, count=0, maps={}):
#     print(v, 'solution2')
#     if v == 1:
#         return count
#     count +=1
#     candidates = []
#     if v % 5 == 0:
#         if (v // 5) in maps:
#             candidates.append(maps[v // 5])
#         else:
#             result = solution2(v // 5, count)
#             maps[v // 5] = result
#             candidates.append(result)
#     elif v % 3 == 0:
#         if (v // 3) in maps:
#             candidates.append(maps[v // 3])
#         else:
#             result = solution2(v // 3, count)
#             maps[v // 3] = result
#             candidates.append(result)
#     elif v % 2 == 0:
#         if (v // 2) in maps:
#             candidates.append(maps[v // 2])
#         else:
#             result = solution2(v // 2, count)
#             maps[v // 2] = result
#             candidates.append(result)
#     if (v - 1) in maps:
#         candidates.append(maps[v - 1])
#     else:
#         result = solution2(v - 1, count)
#         maps[v - 1] = result
#         candidates.append(result) 
#     return min(candidates)

# print(solution2(26))