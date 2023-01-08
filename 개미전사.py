#식량 창고의 개수
x = int(input())
#각 식량 창고에 저장된 식량의 개수
x_list = list(map(int, input().split()))

best = [0]*100

best[0] = x_list[0]
best[1] = max(x_list[0], x_list[1])
for i in range(2, x):
    best[i] = max(best[i-1], best[i-2]+x_list[i])
print(best[x-1])