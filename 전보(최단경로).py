import heapq
n, m, start = map(int, input().split())
INF = int(1e9)
# distance와 gragh를 만든다.
distance = [INF] * (n+1)
graph = [[] for i in range(n+1)]
# 간선 정보를 넣는다.
for i in range(m):
    a, b, c  = map(int, input().split())
    graph[a].append((b, c))

# 알고리즘 실행
q = []
heapq.heappush(q, (0,start))
distance[start] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = i[1] + dist
        if distance[i[0]] > cost:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
city_num = 0
time = 0
for i in range(1, n+1):
    if distance[i] != INF:
        city_num += 1
        time = max(time, distance[i])
print(distance)
print(city_num, time)