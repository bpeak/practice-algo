# 객체지향적으로도 풀어볼까요오

def solution(answers):
	supo1 = [1,2,3,4,5]
	supo1_len = len(supo1)
	supo2 = [2,1,2,3,2,4,2,5]
	supo2_len = len(supo2)
	supo3 = [3,3,1,1,2,2,4,4,5,5]
	supo3_len = len(supo3)

	counts = [0, 0, 0]

	for i, answer in enumerate(answers):
		if answer == supo1[i % supo1_len]:
			counts[0] += 1
		if answer == supo2[i % supo2_len]:
			counts[1] += 1
		if answer == supo3[i % supo3_len]:
			counts[2] += 1

	count_max = max(counts)
	return [i + 1 for i, v in enumerate(counts) if v == count_max]

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))