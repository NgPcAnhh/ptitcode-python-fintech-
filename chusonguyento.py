def check(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

for _ in range(int(input())):
    n = int(input())
    b = len(str(n))
    lis = list(str(n))
    a = []
    for i in lis:
        a.append(check(int(i)))
    if check(b) and a.count(True) >= len(a) / 2:
        print("YES")
    else:
        print("NO")
