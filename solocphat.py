def check_number(n):
    numbers = ['688', '68', '6']  
    n = str(n)
    for num in numbers:
        n = n.replace(num, '') 
    if len(n) == 0: 
        print("YES")
    else:
        print("NO")

n = int(input())
check_number(n)
