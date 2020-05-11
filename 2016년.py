# me
daysOfMonth = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}
days = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
def solution(month, day):
    diffDays = 0
    for i in range(1, month):
        diffDays += daysOfMonth[i]
    diffDays += day - 1
    return days[diffDays % len(days)]
print(solution(1, 8)) # FRI
print(solution(5, 24)) # TUE

"""
1) python god 슬라이싱 a[start : end : step]
2) 일관성 ( daysOfMonth 도 인덱스면 충분한거 아닐까? )
3) 스트림
"""

# best
daysOfMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
def solution2(month, day):
	return days[(sum(daysOfMonth[:month - 1]) + day - 1) % 7]

print(solution2(1, 8)) # FRI
print(solution2(5, 24)) # TUE