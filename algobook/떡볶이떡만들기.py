# 정렬 후 보기
def solution(heights, target_height):
    heights.sort(reverse=True)
    max_height = heights[0]
    loop_count = 0
    cal_count = 0
    for cutter_height in range(max_height, 0 - 1, -1):
        total_height = 0
        loop_count += 1
        for height in heights:
            total_height += height - cutter_height
            cal_count += 1
            if total_height >= target_height:
                print(f'loop: {loop_count}, cal: {cal_count}')
                return cutter_height

print(solution(heights=[19, 15, 10, 17], target_height=6))

# 조기 탈출
def solution2(heights, target_height):
    heights.sort(reverse=True)
    max_height = heights[0]
    cal_count = 0
    loop_count = 0
    for cutter_height in range(max_height, 0 - 1, -1):
        total_height = 0
        loop_count += 1
        for height in heights:
            cal_count += 1
            total_height += height - cutter_height
            if total_height < target_height and height - cutter_height <= 0:
                break
            if total_height >= target_height:
                print(f'loop: {loop_count}, cal: {cal_count}')
                return cutter_height

print(solution2(heights=[19, 15, 10, 17], target_height=6))

# 이진탐색
def solution_bs(heights, target_height):
    heights.sort(reverse=True)
    max_height = heights[0]
    start = 0
    end = max_height

    last_max = None

    loop_count = 0
    cal_count = 0
    while start <= end:
        loop_count += 1
        mid = (start + end) // 2
        # result = sum([height - mid for height in heights if height - mid > 0])
        result = 0
        for height in heights:
            cal_count += 1
            if height - mid > 0:
                result += height - mid
        if result == target_height:
            print(f'loop: {loop_count}, cal: {cal_count}')
            return mid
        elif result > target_height:
            last_max = mid
            start = mid + 1
        else:
            end = mid - 1
    print(f'loop: {loop_count}, cal: {cal_count}')
    return last_max

print(solution_bs(heights=[19, 15, 10, 17], target_height=6))

# 이진탐색2
def solution_bs2(heights, target_height):
    heights.sort(reverse=True)
    max_height = heights[0]
    start = 0
    end = max_height

    last_max = None

    loop_count = 0
    cal_count = 0
    while start <= end:
        loop_count += 1
        mid = (start + end) // 2

        result = 0
        for height in heights:
            cal_count += 1
            if height - mid > 0:
                result += height - mid
            else:
                if result < target_height:
                    break

        if result == target_height:
            print(f'loop: {loop_count}, cal: {cal_count}')
            return mid
        elif result > target_height:
            last_max = mid
            start = mid + 1
        else:
            end = mid - 1
    print(f'loop: {loop_count}, cal: {cal_count}')
    return last_max

print(solution_bs2(heights=[19, 15, 10, 17], target_height=6))