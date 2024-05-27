import re

def filter_digits(test_cases):
    results = []
    for test in test_cases:
        # Sử dụng biểu thức chính quy để tách chuỗi thành các phần tử chỉ chứa số
        numbers = re.split('\D+', test)
        # Loại bỏ các phần tử rỗng và chuyển đổi các phần tử còn lại thành số nguyên
        numbers = [int(num) for num in numbers if num]
        results.append(numbers)
    return results

T = int(input().strip())  # Số lượng bộ test
test_cases = [input().strip() for _ in range(T)]  # Nhập các bộ test
filtered_results = filter_digits(test_cases)  # Lọc ra các số từ các bộ test

# In ra giá trị nhỏ nhất của từng list
for result in filtered_results:
    print(max(result))
