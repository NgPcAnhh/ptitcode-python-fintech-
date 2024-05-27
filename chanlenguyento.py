import math
def check(n):
    n = str(n)
    for i in range(len(n)):
        if i % 2 != 0 and int(n[i]) % 2 == 0:
            return 0
        elif i % 2 == 0 and int(n[i]) % 2 != 0:
            return 0
    return 1

def check1(n):
    if n < 3:
        return 1
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0 :
            return 0
    return 1

for i in range(int(input())):
    n = int(input())
    a = [int(chu_so) for chu_so in str(n)]
    b = sum(a)
    if check(n) and check1(b):
       print("YES")
    else:
        print("NO")
