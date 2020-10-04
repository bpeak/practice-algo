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