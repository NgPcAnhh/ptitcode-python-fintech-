n = int(input())
m = list(map(int, input().split()))
a = []

for i in range(min(m), max(m)+1):
    if i not in m:
        a.append(i)
if a:
    print(min(a))
else:
    print(max(m) + 1)
