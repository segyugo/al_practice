#두 배열의 원소 교체
#N개의 배열 a, b를 가지고 있다.
#K번만큼 a와 b의 원소를 바꿔치기 할 수 있다.
#A원소의 합이 최대가 되는게 목표이다.

N, K = map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break
print(sum(A))







"""
5 3
4 5 6 2 1
7 8 6 2 1
"""