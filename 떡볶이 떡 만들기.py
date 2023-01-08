# N(떡의 개수), x(요청한 떡의 길이)
n, x = map(int, input().split())
# 각각 떡의 길이 length
length = list(map(int, input().split()))

start = 0

# 반복문
while start <= end:

    mid = (start + end) // 2
    mid_result = 0
    for i in length:
        if i > mid:
            mid_result += i - mid
    if mid_result > x:
        result = mid
        start = mid + 1
        continue
    elif mid_result <= x:
        end = mid - 1
        continue
print(result)
    #mid > x
#mid < x