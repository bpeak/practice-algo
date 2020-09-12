def solution(host_parts, guest_parts):
    host_parts_set = set(host_parts)
    return ['yes' if part in host_parts_set else 'no' for part in guest_parts]

def solution2(host_parts, guest_parts):
    host_parts.sort()
    result = []
    for guest_part in guest_parts:
        start = 0
        end = len(host_parts) - 1
        while start <= end:
            mid = (start + end) // 2
            if host_parts[mid] == guest_part:
                result.append('yes')
                break
            if host_parts[mid] > guest_part:
                end = mid - 1
            else:                
                start = mid + 1
        else:
            result.append('no')
    return result

print(solution([8,3,7,9,2], [5,7,9]))
print(solution2([8,3,7,9,2], [5,7,9]))