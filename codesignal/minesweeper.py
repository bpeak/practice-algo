def minesweeper(matrix):
    result = []
    for r in range(0, len(matrix)):
        result_row = []
        for c in range(0, len(matrix[r])):
            s = 0
            for dr, dc in ((-1, 1), (0, 1), (1, 1), (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0)):
                if r + dr < 0 or c + dc < 0: continue
                try:
                    s += matrix[r + dr][c + dc]
                except:
                    continue
            result_row.append(s)
        result.append(result_row)
    return result

print(minesweeper([
    [True, False, False],
    [False, True, False],
    [False, False, False]])) # [[1, 2, 1], [2, 1, 1], [1, 1, 1]]

print(minesweeper([
    [True,False,False,True], 
    [False,False,True,False], 
    [True, True, False, True]]))
    
"""
const directions = [
    [ 1,-1], [ 1, 0], [ 1, 1],
    [ 0,-1],          [ 0, 1],
    [-1,-1], [-1, 0], [-1, 1]
];
"""