def solution(n, computers):
    visited = set()
    count = 0
    for start_idx in range(len(computers)):
        if start_idx not in visited:
            count += 1
            stack = [start_idx]
            visited.add(start_idx)
            while len(stack) > 0:
                curr_idx = stack.pop()
                for adj_idx in range(len(computers[curr_idx])):
                    if computers[curr_idx][adj_idx] == 1 and adj_idx not in visited:
                        stack.append(adj_idx)
                        visited.add(adj_idx)
    return count                        

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 1