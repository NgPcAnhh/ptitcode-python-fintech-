def check(n):
    str_n = str(n)
    if len(str_n) % 2 != 0:
        return False
    return str_n == str_n[::-1]
def check1(n):
    str_n = str(n)
    for i in str_n:
        if int(i) % 2 != 0:
            return False
    return True
for _ in range(int(input())):
    s = int(input())
    for i in range(22, s, 2):
        str_i = str(i)
        if check(str_i) and check1(str_i):
            print(i, end=" ")
    print()
