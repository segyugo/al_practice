N = int(input())
address = []
for i in range(N):
    address.append(list(map(int, input())))
ad_num = 0
n = []

def search(x, y):
    if (x< 0 or y < 0 or x >= N  or y >= N):
        return False
    if address[x][y] == 0:
        return False
    address[x][y] = 0
    global count
    count += 1
    search(x-1, y)
    search(x+1, y)
    search(x, y-1)
    search(x, y+1)
    return True


# 모든 부분 전부 탐색
count = 0
for i in range(N):
    for j in range(N):
        if search(i, j):
            ad_num += 1
            n.append(count)
            count = 0
print(ad_num)
n.sort()
for i in n:
    print(i)

