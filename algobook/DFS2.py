# * 반복문 돌려놓고 들어간다 *

def dfs(graph, v, visited=set()):
    start_v = 1
    stack = [start_v]
    visited.add(start_v)
    while len(stack) > 0:
        curr_v = stack.pop()
        print(f'방문 {curr_v}')
        for adj_v in graph[curr_v]:
            if adj_v not in visited:
                stack.append(adj_v)
                visited.add(adj_v)
        

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