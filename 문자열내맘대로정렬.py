from functools import cmp_to_key

def solution(strings, n):
	def compare(a, b):
		if a[n] > b[n]:
			return 1
		elif a[n] == b[n]:
			if a > b:
				return 1
			else:
				return -1
		else:
			return -1

	return sorted(strings, key=cmp_to_key(compare))

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))