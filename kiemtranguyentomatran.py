import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def fix_matrix(matrix):
    for row in matrix:
        for i in range(len(row)):
            if is_prime(row[i]):
                row[i] = 1
            else:
                row[i] = 0
    return matrix

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

fixed_matrix = fix_matrix(matrix)
for row in fixed_matrix:
    print(*row)

