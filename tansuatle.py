from collections import Counter

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    s = set() 
    counts = Counter(l)
    for i in l:
        if counts[i] % 2 == 1:
            s.add(i)

    for i in s:
        print(i)
