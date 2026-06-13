class person:
    def __init__(self,name,age,height,gender):
        self.__name=name
        self.__age=age
        self.__height=height
        self.__gender=gender
    def __str__(self):
        return f"Name : {self.__name} \nage: {self.__age }\nHeight : {self.__height} \nGender : {self.__gender}"
    
    def update(self,Age=None, Height=None):
        if Age is not None:
            self.__age = Age
        if Height is not None:
            self.__height = Height
    
    def __gt__(self, other): #overload of greater than symbol (>)
        return self.__age>other.__age
   
        
s1=person("abc",19,170,"M")
# print(s1)
s2=person("xyz",20,165,"F")
print(s1>s2)

#you are giving new meaning for this "Greater Than" symbol becuase it's not gonna work for "structures" 