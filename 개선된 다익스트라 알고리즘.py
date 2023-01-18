import heapq
#무한을 가르키는 INF
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
distance = [INF] * (n+1)
gragh = [[] for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    gragh[a].append((b, c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in gragh[now]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])