from collections import deque

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end= "\n")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                print(queue)


graph = [[], [2, 3], [1], [1, 4], [3]]
visited = [False]*9
BFS(graph, 1, visited)