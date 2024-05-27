import math
for i in range(int(input())):
    N,X,M = map(float,input().split())
    T = math.log(M/N, 1+X/100)
    print(math.ceil(T))