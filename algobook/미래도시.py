def solution(infos, n, x, k):
    INF = 1e9
    graph = [[INF] * (n + 1) for i in range(n + 1)]

    for i in range(n + 1):
        graph[i][i] = 0

    for s, d in infos:
        graph[s][d] = 1
        graph[d][s] = 1

    for k in range(n + 1):
        for i in range(n + 1):
            for j in range(n + 1):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    return graph[1][k] + graph[k][x]
                    
print(solution(((1,2), (1,3), (1,4), (2,4), (3,4), (3,5), (4,5)), 5, 4, 5))

# INF = 1e9
# graph = [[INF] * 5 for i in range(5)]
# print(graph)

# graph[1][2] = 2
# graph[2][3] = 3
# graph[3][4] = 10

# for k in range(5):
#     for i in range(5):
#         for j in range(5):
#             if graph[i][k] + graph[k][j] < graph[i][j]:
#                 graph[i][j] = graph[i][k] + graph[k][j]

# for row in graph:
#     print(row)

# print(graph[1][4])