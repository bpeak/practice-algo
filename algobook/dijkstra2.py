INF = 987654321

def solution(graph, node_count):
    distances = [INF] * (node_count + 1)
    visited = [False] * (node_count + 1)
    start_node_num = 1
    visited[start_node_num] = True
    distances[start_node_num] = 0
    for adj_node in graph[start_node_num]:
        adj_node_num, adj_node_distance = adj_node
        distances[adj_node_num] = adj_node_distance
    for i in range(node_count - 1):
        smallist_node_num = None
        smallist_node_distance = INF
        for node_num in range(1, len(graph)):
            if visited[node_num] == False and distances[node_num] < smallist_node_distance:
                smallist_node_distance = distances[node_num]
                smallist_node_num = node_num
        curr_node_num = smallist_node_num
        visited[curr_node_num] = True
        for adj_node in graph[curr_node_num]:
            adj_node_num, adj_node_distance = adj_node
            calculated_distance = distances[curr_node_num] + adj_node_distance
            if calculated_distance < distances[adj_node_num]:
                distances[adj_node_num] = calculated_distance
    print(distances)

solution([[], [[2,2], [3,5], [4,1]], [[3,3], [4,2]], [[2,3], [6,5]], [[3,3], [5,1]], [[3,1], [6,2]]], 6)
