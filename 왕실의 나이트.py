#문자열을 받고 이를 좌표로 치환

# 차이점1. 문자열 인덱싱 & ord를 통해 간단하게 좌표로 치환
a = input()
x = int(ord(a[0])-ord('a'))+1
y = int(a[1])
count = 0
#좌표를 8개의 케이스별로 움직임
# 좌표를 하나로 만들어 리스트로 반복문을 돌려 코드가 간단해짐
move = [(-2, -1),(-2, 1),(2, -1),(2, 1),(-1, -2),(-1, 2),(1, -2),(1, 2)]
for i in move:
    nx = x + i[0]
    ny = y + i[1]
    if nx <=0 or ny <=0 or nx > 8 or ny>8:
        continue
    count += 1
print(count)
#차이점 1