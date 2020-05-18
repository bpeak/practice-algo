def solution(matrix1, matrix2):
	resultMatrix = []
	for rowIdx, row in enumerate(matrix1):
		resultRow = []
		for colIdx, value in enumerate(row):
			resultValue = value + matrix2[rowIdx][colIdx]
			resultRow.append(resultValue)
		resultMatrix.append(resultRow)
	return resultMatrix

print(solution([[1,2], [2,3,]], [[3,4], [5,6]]))