def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_coprime(a, b):
    return gcd(a, b) == 1

def find_coprimes(N, K):
    lower_limit = 10**(K-1)
    upper_limit = min(N, 10**K)
    coprimes = [i for i in range(lower_limit, upper_limit) if is_coprime(N, i)]
    return coprimes

def print_coprimes(coprimes):
    for i in range(0, len(coprimes), 10):
        print(' '.join(map(str, coprimes[i:i+10])))

N, K = map(int, input().split())
coprimes = find_coprimes(N, K)
print_coprimes(coprimes)
