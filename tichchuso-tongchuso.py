for _ in range(int(input())):
    n = input()
    b = [int(n[i]) for i in range(len(n)) if i % 2 == 0 and int(n[i]) != 0]
    a = [int(n[i]) for i in range(len(n)) if i % 2 != 0 ]
    tong = sum(a)
    result = 1
    if len(b) != 0:
        for i in b:
            result *= i
    else:
        result = 0
    print(result,tong)
