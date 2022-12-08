from collections import deque

#정보받기
n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x = 1, y = 1):
    queue = deque()
    queue.append((x, y))
    while queue:
        v = queue.popleft()
        for i in range(4):
            if graph[v[0]+dx[i]][v[1]+dy[i]] == 1:
                #넣고
                queue.append((v[0]+dx[i], v[1]+dy[i]))
                #더하고
                graph[v[0]+dx[i]][v[1]+dy[i]] = graph[v[0]][v[1]]



bfs(1, 1)
print(graph[n-1][m-1])






#무조건 오른쪽, 아래로 가는게 이득 간길은 2로 표시한다
#만약 오른쪽 아래가 0이라면 위나 아래로 돌아가야 한다.
#갔던길을 다시 돌아가야 한다면 이는 잘못된 길이다. 이는 0으로 표시
# 마지막 좌표를 찍으면 성공
#2의 개수를 세기