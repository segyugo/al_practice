def binary_search(array, target, start, end):
    # 1.처음과 끝의 중간 값을 찾고
    mid = (start + end) // 2
    if target == array[mid]:
        return mid
    #2.탐색 값이 중간 값보다 크면
    if target > array[mid]:
        return binary_search(array, target, mid +1 , end)
    #3 탐색값이 중간 값보다 작으면
    if target < array[mid]:
        return binary_search(array, target, start, mid -1)


n, target = map(int, input().split())
array = list(map(int, input().split()))

print(binary_search(array, target, 0, n-1)+1, '번째 값 입니다')