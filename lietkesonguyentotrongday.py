import math
def check(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n = int(input())
m = list(map(int, input().split()))
a = []
for i in m:
    if check(i):
        a.append(i)

count_dict = {}
for num in a:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# In ra từ điển
for num, count in count_dict.items():
    print(num, count)
