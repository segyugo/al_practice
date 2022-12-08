#DFS는 최대한 멀리있는 노드를 우선으로 탐색
def dfs(graph, v, visited):
    #방문처리
    visited[v] = True
    print(v, end = "")
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, visited[i], visited)