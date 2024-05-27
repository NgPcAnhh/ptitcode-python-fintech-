n = int(input())

a = [[]] * n

for i in range(n):
    a[i] = [int(x) for x in input().split()]

above = 0 
below = 0

for i in range(n):
    for j in range(n):
        if i > j:
            below += a[i][j]
        elif i < j:
            above += a[i][j]

s = above - below
summ = abs(s)

x = int(input())
if s <= x:
    print("YES")
else:
    print("NO")
print(summ)
