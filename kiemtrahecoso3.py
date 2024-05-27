def check(n):
    check_list = ['1', '2', '0']
    for item in n:
        if item not in check_list:
            return "NO"
    return "YES"

s = int(input())
for i in range(s):
    n = str(input())
    print(check(n))
