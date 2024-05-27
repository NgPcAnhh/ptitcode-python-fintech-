a = int(input())
bo_so = []
for i in range(a):
    nhap_so = input()
    bo_so.append(nhap_so)

for n in bo_so:
    if n[0] == n[-1]:
        print("YES")
    else:
        print("NO")
    
    