from collections import Counter

def prime_factors(n):
# kiểm tra những số nguyên tố mà số input chia hết 
    i = 2
    factors = []
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
    terms = ["1"] + [f"{factor}^{count}" 
                     if count > 1 
                     else f"{factor}^1" 
                     for factor, count in factor_counts.items()]
    return " * ".join(terms)



n = int(input())
for _ in range(n):
    s = int(input())
    factors = prime_factors(s)
    expression = format_expression(factors)
    print(expression)
