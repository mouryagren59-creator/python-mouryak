class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def details(self):
        print(f"{self.x}+{self.y}i")

    def add(self, other):
        other.x=self.x+other.x
        other.y=self.y+other.y
        return other
    def sub(self, other):
        other.x=self.x-other.x
        other.y=self.y-other.y
        return other
    def mult(self, other):
        real=(self.x*other.x)-(self.y*other.y)
        imag=(self.x*other.y)+(self.y*other.x)
        return Complex(real,imag)
    def magnitude(self):
        return(((self.x**2)+(self.y**2))**0.5)



c1 = Complex(3, 4)
c1.details()

c2 = Complex(1, 2)
c2.details()

c3=Complex(1, 2)
c3.details()

print(c1.magnitude())

