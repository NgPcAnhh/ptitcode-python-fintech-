import math
from collections import Counter

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def nhung_so_nguyento(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def format_expression(factors):
    factor_counts = Counter(factors)
    terms = ["1"] + [f"{factor}^{count}" for factor, count in factor_counts.items()]
    return " * ".join(terms)

n = int(input())
for i in range(n):
    num = int(input())
    f = nhung_so_nguyento(num)
    e = format_expression(f)
    print(e)
