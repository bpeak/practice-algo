# * 반복문 돌려놓고 들어간다 *

def dfs(graph, v, visited=set()):
    print(f'{v} 방문')
    visited.add(v)

    for v_ in graph[v]:
        if v_ not in visited:
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
], 1)