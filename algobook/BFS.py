from collections import deque

def dfs(graph, start_v):
    queue = deque()
    visited = [False] * 9
    queue.append(start_v)
    visited[start_v] = True

    while len(queue) != 0:
        v = queue.popleft()
        print(f'{v}')       
        for v_ in graph[v]:
            if not visited[v_]:
                queue.append(v_)
                visited[v_] = True

dfs([
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],
], 1)