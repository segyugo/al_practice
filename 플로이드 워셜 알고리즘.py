n, m = map(int, input().split())
INF = int(1e9)

gragh = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    gragh[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    gragh[a][b] = c

for k in range(1, n+1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            gragh[a][b] = min(gragh[a][b], gragh[a][k] + gragh[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if gragh[a][b] == INF:
            print("INF", end = " ")
        else:
            print(gragh[a][b], end = " ")
    print()