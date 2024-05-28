class ho:
    def __init__(self, sophong, matoanha, tenchuho, soKwh):
        self.sophong = sophong
        self.matoanha = matoanha
        self.tenchuho = tenchuho
        self.soKwh = soKwh
        
    def tinh_tongtien(self):
        summ = 0
        if self.soKwh <= 100:
            summ = self.soKwh * 1450
        elif 101 <= self.soKwh <= 150:
            summ = 100 * 1450 + (self.soKwh - 100) * 1750
        elif self.soKwh >= 151:
            summ = 100 * 1450 + 50 * 1750 + (self.soKwh - 150) * 2000
        return round(summ * 1.1,2)

    def output(self):
        return self.sophong, self.matoanha, self.tenchuho, self.soKwh, self.tinh_tongtien()
    
if __name__ == '__main__':  
    result = []
    while True:
        sophong = input("nhập số phòng: ")
        matoanha = input("nhập mã tòa nhà: ")
        tenchuho = input("nhập tên chủ hộ: ")
        soKwh = input("nhập số Kwh được sử dụng: ")

        # Check if any of the inputs are empty or soKwh is less than 0
        if not sophong or not matoanha or not tenchuho or not soKwh or float(soKwh) < 0:
            print("Đã nhập sai hoặc thiếu thông tin, vui lòng thử lại.")
            break

        canho = ho(sophong, matoanha, tenchuho, float(soKwh))
        result.append(canho.output())

        cont = input("Bạn có muốn nhập thêm không? (nhập 'không' để dừng): ")
        if cont.lower() == 'không':
            break

    with open('output.txt', 'w') as f:
        f.write("{:<10} {:<10} {:<15} {:<10} {:<15}\n".format('sophong', 'matoanha', 'tenchuho', 'soKwh', 'tinh_tongtien'))
        for i in result:
            f.write("{:<10} {:<10} {:<15} {:<10} {:<15}\n".format(*i))

"""
    print("{:<10} {:<10} {:<15} {:<10} {:<15}".format('sophong', 'matoanha', 'tenchuho', 'soKwh', 'tinh_tongtien'))
    for i in result:
        print("{:<10} {:<10} {:<15} {:<10} {:<15}".format(*i))
"""