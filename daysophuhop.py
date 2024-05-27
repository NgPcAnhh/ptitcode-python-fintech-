t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    if all(i <= j for i, j in zip(a, b)):
        print("YES")
    else: 
        print("NO")

