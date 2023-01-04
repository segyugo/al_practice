# 총 부품 종류 n
n = int(input())
# 매장의 전체 부품 리스트 store
store = list(map(int, input().split()))
# 구매 부품 종류 m
m =  int(input())
# 구매 원하는 부품 리스트 sell
sell = list(map(int, input().split()))
# 전체 부품 정렬
store.sort()
# 각 부품을 반복문 안에 넣기
for target in sell:
    start = 0
    end = n - 1
    while True:
        mid = (start + end) // 2
        if start > end:
            print("no")
            break
        if target == store[mid]:
            print("yes")
            break
        if target < store[mid]:
            end = mid -1

        if target > store[mid]:
            start = mid +1




