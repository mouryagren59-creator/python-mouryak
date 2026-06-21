class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
class square(rectangle):
    def __init__(self,side):
        self.a = side
    def area_2(self):
        return self.a*self.a

s1 = square(5)
print(s1.area())