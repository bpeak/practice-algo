def solution(row, col, matrix):
    total_max = -1
    for row in matrix:
        curr_row_min = min(row)
        if curr_row_min > total_max:
            total_max = curr_row_min
    return total_max

print(solution(3, 3, [[3,1,2],[4,1,4],[2,2,2]]))
print(solution(2, 4, [[7,3,1,8],[3,3,3,4]]))