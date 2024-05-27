for _ in range(int(input())):
    n = input().split('.')
    l = []
    for i in n:
        if i.isdigit() and 0 <= int(i) <= 255:
            l.append(i)
    if len(l) == 4:
        print("YES")
    else:
        print("NO")
