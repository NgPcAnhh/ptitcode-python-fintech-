import itertools

a, b = map(int, input().split())

def ucln(a, b):
    while b:
        a, b = b, a % b
    return a

def check(bo):
    a,b,c = bo
    return ucln(a, b) == 1 and ucln(a, c) == 1  and ucln(b, c) == 1


day_so = list(range(a, b+1)) 
for bo in itertools.combinations(day_so,3):
    if check(bo): 
        print(bo)
