def check(n):
  if n < 1:
    return 0
  i = 2
  while i * i <= n:
    if n % i == 0:
      return 0
    i += 1
  return 1


for i in range(int(input())):
    n = input()
    s = [int(chu_so) for chu_so in str(n)]
    p = sum(s)
    if check(p):
        print("YES")
    else:
        print("NO")