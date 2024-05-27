import math

class phanso:
    def __init__(self, tuso, mauso):
        self.tuso = int(tuso)
        self.mauso = int(mauso)

    def rutgonphanso(self):
        ucln = math.gcd(self.tuso, self.mauso)
        self.tuso = self.tuso // ucln
        self.mauso = self.mauso // ucln

    def output(self):
        self.rutgonphanso()
        return str(self.tuso) + "/" + str(self.mauso)
    

if __name__ == '__main__':
    result = []
    a, b = input().split()
    botest = phanso(a,b)
    result.append(botest.output())

    for i in result:
        print(i)
