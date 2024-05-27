def round_decimal(num):
    num_str = str(num)
    decimal_point_position = num_str.index('.')
    arr = [int(i) for i in num_str.replace('.', '')]    
    for i in range(len(arr) - 1, decimal_point_position, -1):
        if arr[i] >= 5:
            arr[i - 1] += 1
        arr[i] = 0
    if arr[decimal_point_position] == 10:
        arr[decimal_point_position] = 0
        arr[decimal_point_position - 1] += 1
    rounded_num_str = ''.join(str(i) for i in arr)
    rounded_num_str = rounded_num_str[:decimal_point_position] + '.' + rounded_num_str[decimal_point_position:]
    rounded_num = float(rounded_num_str)
    return rounded_num


def diemtb(n):
    tb = (n[0] + n[1] + sum(n))/(len(n)+2)
    tb = round_decimal(tb)
    if tb >= 9:
        return tb, 'XUAT SAC'
    elif tb >= 8 and tb <= 8.9:
        return tb, 'GIOI'
    elif tb >= 7 and tb <= 7.9:
        return tb, 'KHA'
    elif tb >= 5 and tb <= 6.9:
        return tb, 'TB'
    else:
        return tb, 'YEU'

n = int(input())
ds = []
for i in range(1, n+1):
    ten = input()
    diem = list(map(float, input().split()))
    mahs = f"HS{i:02d} {ten}"
    tb, xl = diemtb(diem)
    ds.append((mahs, tb, xl))  

ds.sort(key=lambda x: (x[0]))
ds.sort(key=lambda x: (-x[1]))  

for mahs, tb, xl in ds:
    print(f"{mahs} {round_decimal(tb)} {xl}")  
