def fibonacci(x, y):
    a = [0, 1]
    while len(a) < (y+1):
        a.append(a[-1] + a[-2])
    return a[x:y+1]  

for i in range(int(input())):
    a, b = list(map(int, input().split()))
    fib_sequence = fibonacci(a, b)
    print(' '.join(map(str, fib_sequence)))
