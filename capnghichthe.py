
c =int(input())
a = list(map(int,input().split()))
n = len(a)
b = []
for x in range(n):
    for y in range(x+1, n):
        if a[x] > a[y]: 
            b.append((x,y))
print(len(b))
 