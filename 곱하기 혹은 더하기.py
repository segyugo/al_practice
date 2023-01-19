a = input()

sum = 1
for j in a:
    i = int(j)
    if i <= 1:
        sum += i
    else:
        sum *= i

print(sum)