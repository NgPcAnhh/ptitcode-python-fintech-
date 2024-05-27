def check(n):
  if n <= 1:
    return [n]

  thua_so_nguyen_to = []
  i = 2
  while i * i <= n:
    while n % i == 0:
      thua_so_nguyen_to.append(i)
      n //= i
    i += 1

  if n > 1:
    thua_so_nguyen_to.append(n)

  return thua_so_nguyen_to

result = 0
for i in range(int(input())):
    n = int(input())
    m = check(n)
    tong = sum(m)
    result += tong
    
print(result)