for _ in range(int(input())):
    n = int(input()) # số phần tử của dãy
    l = list(map(int, input().split())) # nhập số phần tử
    l.sort()
    summ = 0
    for i in range(1, len(l)):
        if l[i] - l[i-1] != 1 and l[i] - l[i-1] != 0:
            summ += ((l[i] - l[i-1]) -1)
    print(summ )
