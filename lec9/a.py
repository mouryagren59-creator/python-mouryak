class complex:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.count = 0

    def get_details(self):
        self.count+=1
        return f"{self.x}+{self.y}i"
    
    def add(self,other):
        return complex(self.x+other.x, self.y+other.y)
    
c1 = complex(3,2)
print(c1.get_details())
c2 = complex(45,5)
print(c2.get_details())
print((c1.add(c2)).get_details)
