a = int(input())
n = list(map(int, input().split()))
m = list(n)
tong = 0
for i in range(len(m) - 1):
    if m[i] != m[i + 1]:
        tong += 1
    
print(tong)
