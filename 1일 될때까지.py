#숫자를 받는다
N, K = map(int, input().split())
result = 0
# N ==K로 나누어 떨어지는 수가 될때까지 1씩 뺴기
while True:
    target = (N // K) * K
    result += (N-target)
    n = target
#N이 K보다 작을때(더이상 나눌 수 없을때)
    if N < K:
        break
    result += 1
    N//= K

result += n-1
print(result)

