def solution(n, lostStudents, reserveStudents):
    reservedStudents = set()
    for lostStudent in lostStudents:
        n -= 1
        if lostStudent in reserveStudents:
            reservedStudents.add(lostStudent)
            n += 1
            continue
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

print(solution(5, [2,4], [1,3,5])) # 5
print(solution(5, [2,4], [3])) # 4
print(solution(3, [3], [1])) # 2