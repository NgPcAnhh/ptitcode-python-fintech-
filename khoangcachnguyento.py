



import math

def nguyento(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    a = []
    count = 0
    i = 0
    while count < n:
        if nguyento(i):
            a.append(i)
            count += 1
        i += 1
    return a

def generate_sequence(N, X):
    prime_numbers = check(N)
    result = []
    current_number = X
    for gap in prime_numbers:
        result.append(current_number)
        current_number += gap
    return result

N,X = list(map(int,input().split()))

sequence = generate_sequence(N, X)

last_element = sequence[-1] + check(N)[-1]
sequence.append(last_element)

print(*sequence)
