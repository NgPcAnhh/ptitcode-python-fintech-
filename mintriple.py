def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = map(int, input().split())
        sumin = sum(sorted(a)[:3])
        print(sumin)

solve()
