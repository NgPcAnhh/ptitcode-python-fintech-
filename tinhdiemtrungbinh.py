def loc_so(n):
    min_x = min(n) 
    max_x = max(n)
    while min_x in n:
        n.remove(min_x)
    while max_x in n:
        n.remove(max_x)
    return n

def AVG(day_so):
    tong = sum(day_so)
    trung_binh = tong / len(day_so)
    return trung_binh

s = int(input())
n = list(map(float, input().split()))
n = loc_so(n)
m = AVG(n)
a = round(m,2)
    
print(a)
