def tim_uoc_so(n):
    uoc_so = []
    for i in range(1, n + 1):
        if n % i == 0:
            uoc_so.append(i)
    return uoc_so

def la_so_phan_nguyen_to(n):
    uoc_so_n = tim_uoc_so(n)
    for i in range(1, n):
        if len(uoc_so_n) <= len(tim_uoc_so(i)):
            return False
    return True

T = int(input())
for _ in range(T):
    X = int(input())
    X += 1
    while not la_so_phan_nguyen_to(X):
        X += 1
    print(X)
