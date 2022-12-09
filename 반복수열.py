A, P = map(int, input().split())
D = []

while True:
    if(A in D):
        break
    D.append(A)
    Next = 0
    for i in str(A):
        Next += int(i)**P
    A = Next

print(len(D[0:D.index(A)]))

