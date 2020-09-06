def dfs(graph, v, visited):
    print(f'{v} 방문')
    visited[v] = True

    for v_ in graph[v]:
        if not visited[v_]:
            dfs(graph, v_, visited)
        else:
            print(f'{v_} 이미방문')

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
], 1, visited=[False] * 9)