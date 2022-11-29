N, M = map(int, input().split())
full_list = []
final_list = []
#N개의 줄의 입력값을 2차원 리스트로 구현하기
for i in range(N):
    full_list.append(list(map(int, input().split()))) #이떄 +=은 단순히 1차원으로 구성되기에 append를 사용
#각 리스트 간의 최솟값 구함
for i in range(N):
    final_list.append(min(full_list[i]))
#이들중 비교하여 최솟값 선정
print(min(final_list))


