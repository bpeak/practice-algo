# me
def solution(clothes):
    hash_map = {}
    for cloth in clothes:
        cloth_type = cloth[1]
        if cloth_type not in hash_map:
            hash_map[cloth_type] = 0
        hash_map[cloth_type] += 1
    result = 1
    for v in hash_map.values():
        result *= (v + 1)
    result -= 1
    return result

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
# 5

"""
cf>
a = [1,2]
b, c = a
"""

# 파이써닉
from collections import Counter
from functools import reduce

def solution_best(clothes):
	counter = Counter([cloth_type for cloth_name, cloth_type in clothes])
	return reduce(lambda acc, crr: acc * (crr + 1), counter.values(), 1) - 1

print(solution_best([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
#5