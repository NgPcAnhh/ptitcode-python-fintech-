def check_so(n):
    a = list(map(str, str(n)))
    for i in range(0,len(a) - 2):
        if a[i] != a[i + 2]:
            return False
    return True

for i in range(int(input())):
    s = int(input())
    sett = set(str(s))
    if len(sett) == 2 and check_so(s):
        print("YES")
    else:
        print("NO")
