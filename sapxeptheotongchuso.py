def cong(n):
    return sum(int(digit) for digit in str(n))

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    sett = [(i, cong(i)) for i in a]

    sett.sort(key=lambda x: (x[1], x[0]))

    
    for num, _ in sett:
        print(num, end=' ')
    print()
