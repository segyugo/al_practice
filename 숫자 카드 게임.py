N, M = map(int, input().split())

result = 0 # 굳이 리스트로 할 필요 없이 변수에 최솟값을 바로바로 저장하면 된다.
#각 리스트의 최솟값을 구해서 현재의 값과 비교하기
for i in range(N):
    num =  list(map(int, input().split()))
    min_num = min(num)
    result = max(min_num, result)
print(result)
