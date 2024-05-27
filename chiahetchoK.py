a, K, N = map(int,input().split())
results = []  
phanbu_max = int(N/K)*K - a + 1
phanbu_min =( int(a/K)+1)* K -a
if phanbu_max >= phanbu_min:
    for i in range(phanbu_min,phanbu_max,K):
        results.append(str(i))
else:
    results.append("-1")

print(" ".join(results)) 
