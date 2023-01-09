import sys
INF = int(1e9)

#노드 개수와 간선 개수 받기
n, m = map(int,input().split())
#시작 노드 받기
start = int(input())
# 그래프 만들기
graph = [[] for i in range(n+1)]
# 그래프 정보 받기
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
# 1에서 다른 곳으로 가는 최단 거리 그래프 만들기
distance = [INF] * (n+1)
# 방문한 곳 체크하기
visited = [False] * (n+1)

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijk(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
    for j in range(n-1):
        now = get_smallest_node()
        # 방문처리
        visited[now] = True
        # 비용계산
        for k in graph[now]:
            cost = distance[now] + k[1]
        # 비교
            if cost < distance[k[0]]:
                distance[k[0]] = cost

dijk(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("도달 할 수없습니다.")
    else:
        print(distance[i])