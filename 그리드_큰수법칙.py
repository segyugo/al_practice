#N, M, K = map(int, input().split())
N, M, K = 5, 9, 3
#Num = list(map(int, input().split()))
Num = [2, 4, 5, 4, 6]
# sort를 통해 가장 큰 값, 2번쨰로 큰 값 알아내기
Num.sort(reverse=1)
Max = Num[0]
second = Num[1]
#print(Max, second)
# 반복되는 수 총합 구하기
repeat = Max*K + second

repeat_num = repeat * (M//(K+1))

#print(repeat, repeat_num)
# 마지막에 반복되지 않는 나머지 수 더하기
last_num = Max*(M%(K+1))

total = repeat_num + last_num
print(total)