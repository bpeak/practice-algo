def solution(n, lostStudents, reserveStudents):
    reservedStudents = set()
    for lostStudent in lostStudents:
        n -= 1
        front = lostStudent - 1
        back = lostStudent + 1
        if (
            front not in lostStudents and
            front not in reservedStudents and
            front in reserveStudents
        ):
            reservedStudents.add(front)
            n += 1
            continue
        if (
            back not in lostStudents and
            back not in reservedStudents and
            back in reserveStudents
        ):
            reservedStudents.add(back)
            n += 1
            continue
    return n

print(solution(5, [2,4],[1,3,5]))
print(solution(5, [2,4],[3]))
print(solution(3, [3],[1]))


# # def solution(n, lost, reserve):
# #     count = 0
# #     reserved = set()
# #     for i in range(1, n + 1):
# #         if i not in lost:
# #             count += 1
# #             continue
# #         front = i - 1
# #         back = i + 1
# #         if (
# #             front >= 0 and
# #             front not in lost and
# #             front in reserve and
# #             front not in reserved
# #         ):
# #             reserved.add(front)
# #             count += 1
# #             continue
# #         if (
# #             back <= n and
# #             back not in lost and
# #             back in reserve and   
# #             back not in reserved
# #         ):
# #             reserved.add(back)
# #             count += 1
# #             continue            
# #     return count
    
# # print(solution(5, [2,4],[1,3,5]))
# # print(solution(5, [2,4],[3]))
# # print(solution(3, [3],[1]))