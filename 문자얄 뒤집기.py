n = int(input())
m = int(input())
INF = int(1e9)

#각 차원의 길이가 n+1인 그래프를 2차원으로 만든다.
graph = [[INF] * (n+1) for i in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

#해당 차원에 노선 정보를 넣는다.
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

#a를 경유해서 i에서 j로 가는 경로와 기존의 i에서 j까지 갔던 경로를 비교하여
# 작은 값을 넣는다
for a in range(1, n+1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            graph[start][end] = min(graph[start][end], graph[start][a] + graph[a][end])


for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] >= INF:
            print(0, end = " ")
        else:
            print(graph[i][j], end = " ")
    print()