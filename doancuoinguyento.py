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


for i in range(int(input())):
    n = input()
    b = int(n[-4:])
    if check(b):
        print("YES")
    else:
        print("NO")