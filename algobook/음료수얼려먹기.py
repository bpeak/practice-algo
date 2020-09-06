def solution(matrix):
    visited = set()
    count = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def search(matrix, row, col, is_first_access_area=False):
        nonlocal count
        if row > len(matrix) - 1 or \
            row < 0 or \
            col > len(matrix[0]) - 1 or \
            col < 0 or \
            matrix[row][col] == 1:
            return
        if (row, col) not in visited:
            visited.add((row, col))
            if is_first_access_area:
                count += 1
        for d_row, d_col in directions:
            adj_row = row + d_row
            adj_col = col + d_col
            if (adj_row, adj_col) not in visited:
                search(matrix, adj_row, adj_col)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            search(matrix, row, col, True)

    return count

print(solution(matrix=[
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0],
]))

print(solution(matrix=[
    [0,0,0,0,0,1,1,1,1,0,0,0,0,0],
    [1,1,1,1,1,1,0,1,1,1,1,1,1,0],
    [1,1,0,1,1,1,0,1,1,0,1,1,1,0],
    [1,1,0,1,1,1,0,1,1,0,0,0,0,0],
    [1,1,0,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1,1,0,0],
    [1,1,0,0,0,0,0,0,0,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,1,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,0,0,1,1],
    [1,1,1,0,0,0,1,1,1,1,1,1,1,1],
    [1,1,1,0,0,0,1,1,1,1,1,1,1,1]
]))
