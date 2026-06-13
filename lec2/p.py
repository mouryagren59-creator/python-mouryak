class circle():
    def __init__(self,x=0,y=0,r=0):
        self.__x=x
        self.__y=y
        self.__r=r
    def __str__(self):
        return f"Circle radius {self.__r} and origin {(self.__x,self.__y)}"

    def area(self):
        print(f"area = {3.14*(self.__r**2)}")

    def perimeter(self):
        print(f"perimeter = {2*3.14*self.__r}")

c1=circle(1,2,3)
print(c1)
c1.area()
c1.perimeter()