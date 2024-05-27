class Rectangle:
    def __init__(self, chieudai,chieurong, color):
        self.chieudai = int(chieudai)
        self.chieurong = int(chieurong)
        self.color = color

    def perimeter(self):
        return (self.chieudai + self.chieurong) * 2

    def area(self):
        return self.chieudai * self.chieurong
    
    def output(self):
        return self.perimeter(), self.area(), self.color


arr = input().split()
if int(arr[0]) <= 0 or int(arr[1]) <= 0 :
    print("INVALID")
else:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color.capitalize()))
