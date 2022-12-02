#숫자를 받는다
N, M = map(int, input().split())
count = 0
while(N != 1):
    if N%M != 0:
        N -= 1
    elif N%M == 0:
        N = int(N/M)
    count += 1
print(count)

