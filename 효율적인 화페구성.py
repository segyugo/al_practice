n, m = map(int, input().split())
list = []

for i in range(n):
    list.append(int(input()))
d = [10001] * (m+1)

d[0] = 0

for i in range(1, m+1):
    for j in list:
        if i - j >= 0 and d[i - j] < 10001:
            if d[i] > d[i - j] + 1:
                d[i] = d[i - j] + 1

print(d)
print(list)
if d[m] == 10001:
    print(-1)

else:
    print(d[m])











