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

def solution2(matrix):
    visited = set()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def search(matrix, row, col):
        if row > len(matrix) - 1 or \
            row < 0 or \
            col > len(matrix[0]) - 1 or \
            col < 0 or \
            matrix[row][col] == 1 or \
            (row, col) in visited:
            return False
            
        visited.add((row, col))
        for d_row, d_col in directions:
            adj_row = row + d_row
            adj_col = col + d_col
            if (adj_row, adj_col) not in visited:
                search(matrix, adj_row, adj_col)
        return True

    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if search(matrix, row, col) == True:
                count += 1
    return count

def solution3(matrix):
    visited = set()
    ice_count = 0
    def search(matrix, row, col, is_first_access=False):
        nonlocal ice_count
        if  row < 0 or \
            row > len(matrix) - 1 or \
            col < 0 or \
            col > len(matrix[0]) - 1 or \
            matrix[row][col] == 1:
            return
        if (row, col) in visited:
            return
        visited.add((row, col))
        if is_first_access:
            ice_count += 1
        search(matrix, row, col + 1)
        search(matrix, row, col - 1)
        search(matrix, row + 1, col)
        search(matrix, row - 1, col)
            

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            search(matrix, row, col, is_first_access=True)

    return ice_count

def solution4(matrix):
    visited = set()
    def search(matrix, row, col):
        nonlocal ice_count
        if  row < 0 or \
            row > len(matrix) - 1 or \
            col < 0 or \
            col > len(matrix[0]) - 1 or \
            matrix[row][col] == 1:
            return
        if (row, col) in visited:
            return
        visited.add((row, col))
        search(matrix, row, col + 1)
        search(matrix, row, col - 1)
        search(matrix, row + 1, col)
        search(matrix, row - 1, col)
        return True

    ice_count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if search(matrix, row, col) == True:
                ice_count += 1

    return ice_count    

def solution5(matrix):
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                count += 1
                stack = [(row, col)]
                matrix[row][col] = 1 # visit
                while len(stack) > 0:
                    row, col = stack.pop()
                    for dx, dy in directions:
                        next_col = col + dx
                        next_row = row + dy
                        if next_col >= 0 and \
                            next_col <= len(matrix[row]) - 1 and \
                            next_row >= 0 and \
                            next_row <= len(matrix) - 1 and \
                            matrix[next_row][next_col] == 0:
                            matrix[next_row][next_col] = 1
                            stack.append((next_row, next_col))
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


print(solution2(matrix=[
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0],
]))

print(solution2(matrix=[
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

print(solution3([
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]))    

print(solution3(matrix=[
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

print(solution4([
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]))    

print(solution4(matrix=[
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

print(solution5([
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]))    

print(solution5(matrix=[
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
