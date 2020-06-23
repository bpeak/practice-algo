def solution(dartResult):
	scores = []
	skip = False
	for i, c in enumerate(dartResult):
		if skip:
			skip = False
			continue
		if c.isdecimal():
			score_str = c
			next_c = dartResult[i + 1]
			if next_c.isdecimal():
				score_str = c + next_c
				skip = True
			scores.append(int(score_str))		
			continue

		scores_last_idx = len(scores) - 1
		if c == "S":
			continue
		elif c == "D":
			scores[scores_last_idx] **= 2
		elif c == "T":
			scores[scores_last_idx] **= 3
		elif c == "#":
			scores[scores_last_idx] *= -1			
		elif c == "*":
			scores[scores_last_idx] *= 2
			if scores_last_idx > 0:
				scores[scores_last_idx - 1] *= 2
	return sum(scores)

# 1	1S2D*3T	37	11 * 2 + 22 * 2 + 33
# 2	1D2S#10S	9	12 + 21 * (-1) + 101
# 3	1D2S0T	3	12 + 21 + 03
# 4	1S*2T*3S	23	11 * 2 * 2 + 23 * 2 + 31
# 5	1D#2S*3S	5	12 * (-1) * 2 + 21 * 2 + 31
# 6	1T2D3D#	-4	13 + 22 + 32 * (-1)
# 7	1D2S3T*	59	12 + 21 * 2 + 33 * 2
print(solution("1S2D*3T")) 
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))