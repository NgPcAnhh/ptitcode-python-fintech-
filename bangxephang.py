n = int(input())
hs = []

for i in range(n):
    ten = input()
    diem, submit = list(map(int,input().split()))
    hs.append((ten, diem, submit))

# sắp xếp theo tên
hs.sort(key = lambda x: (x[0]))
# sắp xếp theo thứ tự submit từ nhỏ xếp trước lớn
hs.sort(key = lambda x: (x[2]))
# sắp xếp theo thứ tự từ lớn xuống thấp
hs.sort(key = lambda x: (-x[1]))

for i in range(n):
    print(f"{hs[i][0]} {hs[i][1]} {hs[i][2]}")