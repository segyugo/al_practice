#좌표를 받음
a = input()

#문자의 위치를 리스트로 설정
x_list = ["a","b","c","d","e","f","g","h"]
y_list = ['1', '2', '3', '4', '5', '6', '7', '8']
for i in range(8):
    if x_list[i] in a:
        x = i+1
    if y_list[i] in a:
        y = i+1

count = 0
#좌표를 8개의 케이스별로 움직임
x_move = [1,-1, 2, 2, 1,-1,-2,-2]
y_move = [2, 2, 1,-1,-2,-2, 1,-1]
for i in range(len(x_move)):
    nx = x + x_move[i]
    ny = y + y_move[i]
    if nx <=0 or ny <=0 or nx > 8 or ny>8:
        continue
    count += 1
print(count)
#벗어나는건 카운트하지 않음
#출력