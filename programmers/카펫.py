def solution(brown_count, yellow_count):
    total_count = brown_count + yellow_count
    for i in range(total_count, 0, -1):
        width = i
        quotient = total_count // width
        if width * quotient != total_count:
            continue
        height = quotient
        if height < 3:
            continue
        curr_yellow_count = (width - 2) * (height - 2)
        if yellow_count == curr_yellow_count:
            return [width, height]

def solution2(brown_count, yellow_count):
    total_count = brown_count + yellow_count
    for height in range(3, total_count):
        if total_count % height != 0: continue
        width = total_count // height
        curr_yellow_count = (width - 2) * (height - 2)
        if curr_yellow_count == yellow_count:
            return [width, height]

print(solution(10, 2)) # 4 3
print(solution(24, 24)) # 8 6

print(solution2(10, 2)) # 4 3
print(solution2(24, 24)) # 8 6