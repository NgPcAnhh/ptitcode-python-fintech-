def count(b,a):
    a = str(a)
    b = str(b)
    count = 0
    l = len(b)
    i = 0
    while i < len(a) - l + 1:
        if a[i:i+l] == b:
            count += 1
            i += l
        else:
            i += 1  
    return count

for i in range(int(input())):
    a = input()
    b = input()
    c = count(b,a)
    print(c)
