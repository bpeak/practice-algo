from collections import deque

def solution(matrix):
    directions = [(0, 1), (1, 0), (-1 ,0), (0, -1)] # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 이걸로 하면 동작 안함 ( 생각하면 당연 )

    def search(matrix, row, col, stack, visited):
        if row < 0 or \
            row > len(matrix) - 1 or \
            col < 0 or \
            col > len(matrix[0]) - 1 or \
            matrix[row][col] == 0:
            return False
        if (row, col) in visited:
            visited.remove((row, col))
            stack.pop() 
            return False        

        stack.append((row, col))
        visited.add((row, col))

        if row == len(matrix) - 1 and col == len(matrix[0]) - 1:
            return True

        for d_row, d_col in directions:
            adj_row = row + d_row
            adj_col = col + d_col
            if search(matrix, adj_row, adj_col, stack, visited) != False:
                return len(stack)
            else:
                continue

        return False
                
        # if search(matrix, row, col + 1, stack, visited) != False:
        #     return len(stack)
        # if search(matrix, row + 1, col, stack, visited) != False:
        #     return len(stack)
        # if search(matrix, row - 1, col, stack, visited) != False:
        #     return len(stack)
        # if search(matrix, row, col - 1, stack, visited) != False:
        #     return len(stack)
    
    return search(matrix, row=0, col=0, stack=[], visited=set())

def solution2(matrix, x = 0, y = 0):
    directions = [(0, 1), (1, 0), (-1 ,0), (0, -1)]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            next_x = x + dx
            next_y = y + dy
            if next_x <= -1 or \
                next_x >= len(matrix) or \
                next_y <= - 1 or \
                next_y >= len(matrix[0]):
                continue
            if matrix[next_x][next_y] == 0:
                continue
            if matrix[next_x][next_y] == 1:
                matrix[next_x][next_y] = matrix[x][y] + 1
                queue.append((next_x, next_y))
    
    return matrix[len(matrix) - 1][len(matrix[0]) - 1]

print(solution([
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]))

print(solution2([
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]))