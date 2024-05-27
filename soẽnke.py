def check(n):
    n = str(n)   
    first = n[0]  
    for i in range(0, len(n), 2): 
        if n[i] != first:  
            return 0  
    return 1  

for i in range(int(input())):
    n = input()
    if len(n) % 2 != 0 and check(n) and n[0] != n[1]:
        print("YES")
    else:
        print("NO")
