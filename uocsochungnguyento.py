def ucln(a, b):
    while(b):
        a, b = b, a % b
    return a

def tach_so(n):
    return tuple(int(chu_so) for chu_so in str(n))

def la_so_nguyen_to(n):
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

s = int(input())
for i in range(s):
    m,n = map(int,input().split())
    t = ucln(m,n)
    a = tach_so(t)
    b = sum(a)
    if la_so_nguyen_to(b):
        print("YES")
    else:
        print("NO")
        