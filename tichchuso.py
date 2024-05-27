n = int(input())
for i in range(n):
    m = input()
    lis = list(m)
    while '0' in lis:
        lis.remove('0')
    ket_qua = 1
    for chu_so in lis:
        ket_qua *= int(chu_so)
    print(ket_qua)
