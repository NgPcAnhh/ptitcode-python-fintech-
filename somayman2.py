n = int(input())

for i in range(n):
    s = input()
    list_s = list(map(int, str(s)))
    
    # Kiểm tra xem tất cả các số trong danh sách có khác 4 và 7 không
    if any(num != 4 and num != 7 for num in list_s):
        print("NO")
    else:
        print("YES")
