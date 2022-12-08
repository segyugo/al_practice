def recursive_function(n):
    if n <= 1:
        return 1
    print(n, n-1)
    return n*recursive_function(n-1)

print(recursive_function(5))