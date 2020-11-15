def matrixElementsSum(matrix):
    total = 0
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if matrix[i][j] == 0:
                break
            total += matrix[i][j]
    return total

# 9
print(matrixElementsSum([
    [1, 1, 1, 0], 
    [0, 5, 0, 1], 
    [2, 1, 3, 10]
]))

# 9
print(matrixElementsSum([
    [0, 1, 1, 2], 
    [0, 5, 0, 0], 
    [2, 0, 3, 3]
]))

