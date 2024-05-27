import math


def check(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1


for _ in range(int(input())):
    n = input()
    a = int(n[-4:])
    if check(a):
        print("YES")
    else:
        print("NO")