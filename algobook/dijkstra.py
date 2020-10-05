def solution(graph, node_count):
    INF = 1e9
    visited = set()
    distances = [INF] * (node_count + 1)
    distances[1] = 0

    def recur(i, isFrom=False):
        if i > len(graph) - 1: return
        if i in visited: return
        visited.add(i)
        for adjNode, distance in graph[i]:
            calculated_distance = distance + distances[i] if isFrom else distance
            if calculated_distance < distances[adjNode]:
                distances[adjNode] = calculated_distance
        for adjNode, distance in graph[i]:
            recur(adjNode, True)

    for i in range(1, len(graph)):
        recur(i)    

    return distances

print(solution([[], [[2,2], [3,5], [4,1]], [[3,3], [4,2]], [[2,3], [6,5]], [[3,3], [5,1]], [[3,1], [6,2]]], 6))
    


# node_count = 6
# vertex_count = 11

# INF = 1e9
# graph = [[], [[2,2], [3,5], [4,1]], [[3,3], [4,2]], [[2,3], [6,5]], [[3,3], [5,1]], [[3,1], [6,2]]]
# visited = set()
# distances = [INF] * (node_count + 1)
# distances[1] = 0

# def recur(i, i_from=False):
#     if i > len(graph) - 1: return
#     if i in visited: return
#     visited.add(i)
#     for adjNode, distance in graph[i]:
#         calculated_distance = distance + distances[i] if i_from else distance
#         if calculated_distance < distances[adjNode]:
#             distances[adjNode] = calculated_distance
#     for adjNode, distance in graph[i]:
#         recur(adjNode, True)

# for i in range(1, len(graph)):
#     recur(i)

# print(distances)
    
    
    
