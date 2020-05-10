"""
케이스1) 앞학생이 빌려줄 수 있음
케이스2) 뒤학생이 빌려줄 수 있음
케이스3) 내가 여벌을 가져왔음 ( 이 케이스를 빼먹었음 )
"""

def solution(n, lostStudents, reserveStudents):
    lentedStudents = set()
    for lostStudent in lostStudents:
        n -= 1
        if lostStudent in reserveStudents:
            lentedStudents.add(lostStudent)
            n += 1
            continue
        front = lostStudent - 1
        back = lostStudent + 1
        if (
            front not in lostStudents and
            front not in lentedStudents and
            front in reserveStudents
        ):
            lentedStudents.add(front)
            n += 1
            continue
        if (
            back not in lostStudents and
            back not in lentedStudents and
            back in reserveStudents
        ):
            lentedStudents.add(back)
            n += 1
            continue
    return n

print(solution(5, [2, 4], [1, 3, 5])) #5
print(solution(5, [2, 4], [3])) #4
print(solution(3, [3], [1])) #2