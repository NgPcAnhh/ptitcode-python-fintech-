def uoc_so_chung_lon_nhat(a, b):
    while(b):
        a, b = b, a % b
    return a

n = int(input())
for i in range(n):
    a = int(input())
    b = int(str(a)[::-1])
    if uoc_so_chung_lon_nhat(a, b) == 1:
        print("YES")
    else:
        print("NO")
    