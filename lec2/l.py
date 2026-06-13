class person:
    def __init__(self,name,age,height,gender):
        self.name=name
        self.age=age
        self.height=height
        self.gender=gender
    def __str__(self):
        return f"Name : {self.name} \nage: {self.age }\nHeight : {self.height} \nGender : {self.gender}"
    
    def update(self,Age=None, Height=None):
        if Age is not None:
            self.age = Age
        if Height is not None:
            self.height = Height
   
        
s1=person("abc",19,170,"M")
s1.update(Age=20)
print(s1,end=" ")
s1.update(Height=180)
print(s1)