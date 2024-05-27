def check(n):
    m = sum(int(chu_so) for chu_so in str(n))
    if m % 3 == 0:
        return 1
    return 0

for i in range(int(input())):
    n = int(input())
    if check(n):
        print("YES")
    else:
        print("NO")