def boxBlur(matrix):
    result = []
    for i in range(0, len(matrix) - 2):
        r = []
        for j in range(0, len(matrix[i]) - 2):
            v = 0
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    v += matrix[k][l]
            r.append(v // 9)
        result.append(r)
    return result

print(boxBlur([[36,0,18,9], 
        [27,54,9,0], 
        [81,63,72,45]])) # [[40, 30]]

print(boxBlur([[7, 4, 0, 1], 
        [5, 6, 2, 2], 
        [6, 10, 7, 8], 
        [1, 4, 2, 0]])) # [[5, 4], [4, 4]]

print(boxBlur([[1, 1, 1], 
         [1, 7, 1], 
         [1, 1, 1]])) # [[1]]