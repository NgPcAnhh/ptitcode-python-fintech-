from decimal import Decimal
from math import sqrt
# khai báo tọa độ xy
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# tính khoảng cách giữa 2 điểm
    def distance(self, other):
        return sqrt((self.x - other.x)**2 +(self.y - other.y)**2)
# class tam giác
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
# tính chu vi
    def perimeter(self):
        return self.p1.distance(self.p2) + self.p2.distance(self.p3) + self.p3.distance(self.p1)
    
    def output(self):
        return round(self.perimeter(),3)
    
data = []
for i in range(int(input())):
# khai báo số
    arr = list(map(Decimal, input().split()))
    data.append(arr) 

for arr in data:
    p1 = Point(arr[0], arr[1])
    p2 = Point(arr[2], arr[3])
    p3 = Point(arr[4], arr[5])
# gắn vào 3 điểm tam giác
    triangle = Triangle(p1, p2, p3)
# tính chu vi
    cv = triangle.perimeter()
# loại bỏ trường hợp tam giác ko thỏa mãn
    if p1.distance(p2) + p2.distance(p3) <= p3.distance(p1) or p1.distance(p2) + p3.distance(p1) <= p2.distance(p3) or p2.distance(p3) + p3.distance(p1) <= p1.distance(p2):
        print("INVALID")
    else:
        print(triangle.output())

