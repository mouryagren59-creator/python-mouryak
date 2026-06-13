class complex:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __add__(self,other):
        c1=complex()
        c1.x=self.x+other.x
        c1.y=self.y+other.y
        return c1
    def __mul__(self, other):
        c2=complex()
        c2.x=(self.x*other.x)+(-1*(self.y*other.y))
        c2.y=(self.x*other.y)+(self.y*other.x)
        return c2
    def __str__(self):
        return f"{self.x} + {self.y}i"

c1=complex(1,2)
c2=complex(3,2)
c3=c1*c2
print(c3)

#how many operators will not overload and how many operators will overload