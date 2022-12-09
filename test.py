from sys import stdin

A, P = map(int, stdin.readline().split())
check = [A]

while True:
    new = 0
    for i in (str(check[-1])):
        new += int(i) ** P
    if new in check:
        while True:
            if new == check.pop():
                print(len(check))
                exit()
    else:
        check.append(new)