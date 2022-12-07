#방향을 나타낼때는 dx, dy로 나타내는게 효과적이다
n, m = map(int, input().split())
#캐릭터 위치와 방향 설정
d = [[0] * m for _ in range(n)]
#아래와 같이 2차원 리스트는 컴프리헨션을 사용하는게 효율적이다.
x, y, direction = map(int, input().split())
d[x][y] = 1
#맵 생성하기
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
#왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
#시뮬레이션 시작
count = 1
turntime = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        x = nx
        y = ny
        count += 1
        turntime = 0
        continue
    else:
        turn_left()
        turntime += 1
    if turntime == 4:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turntime = 0
print(count)