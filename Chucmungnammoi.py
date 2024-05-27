# Nhập số lượng lời chúc
n = int(input())

# Tạo một set để lưu trữ các lời chúc duy nhất
bo_loi_chuc = set()

# Với mỗi lời chúc
for _ in range(n):
    # Nhập lời chúc
    loi_chuc = input()
    
    # Thêm lời chúc vào set
    bo_loi_chuc.add(loi_chuc)

# In ra số lượng lời chúc duy nhất
print(len(bo_loi_chuc))
