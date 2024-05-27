def check_number(n):
    n = str(n)
    max_num_index = 0
    if len(n) < 3:
       return 'NO' 
   
    # Kiểm tra số sau phải lớn hơn số trước
    for i in range(1, len(n)):
        if n[i] <= n[i-1]:
            max_num_index = i - 1
            break
    else:
        return "YES"

    # Kiểm tra phần còn lại theo thứ tự giảm dần
    if n[max_num_index:] == ''.join(sorted(n[max_num_index:], reverse=True)):
        return "YES"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    print(check_number(n))
