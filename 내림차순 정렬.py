N = int(input())

array = []

for i in range(N):
    array.append(int(input()))

array.sort(reverse=1)

print(array)