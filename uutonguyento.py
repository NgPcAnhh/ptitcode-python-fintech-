def check(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

for _ in range(int(input())):
    n = input()
    l = len(n)
    m = list(n)
    m1 = [int(i) for i in m if check(int(i))]
    m2 = [int(i) for i in m if not check(int(i))]
    if check(l) and len(m1) > len(m2):
        print("YES")
    else: 
        print("NO")
