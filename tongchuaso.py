def count_steps_to_single_digit(n):
    steps = 0
    while len(str(n)) > 1:
        n = sum(int(digit) for digit in str(n))
        steps += 1
    return steps

# Ví dụ sử dụng hàm:
n = int(input("Nhập số nguyên: "))
print("Số bước cần thực hiện:", count_steps_to_single_digit(n))
