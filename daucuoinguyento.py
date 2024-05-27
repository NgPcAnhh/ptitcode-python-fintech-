def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

for _ in range(int(input())):
    n = input()
    a = int(n[0:3])  # Lấy 3 chữ số đầu
    b = int(n[-3:])  # Lấy 3 chữ số cuối
    if is_prime(a) and is_prime(b):
        print("YES")
    else:
        print("NO")
