n, m = map(int, input().split())
INF = int(1e9)
# gragh를 만든다.
gragh = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    gragh[i][i] = 0
# 각 경로를 입력받고 입력 받은 경로를 gragh에 넣는다.
for _ in range(m):
    a, b = map(int, input().split())
    gragh[a][b] = 1
    gragh[b][a] = 1

for j in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n + 1):
            gragh[a][b] = min(gragh[a][b], gragh[a][j] + gragh[j][b])

x, k = map(int, input().split())

if gragh[1][k] + gragh[k][x] > INF:
    print(-1)
else:
    print(gragh[1][k] + gragh[k][x])