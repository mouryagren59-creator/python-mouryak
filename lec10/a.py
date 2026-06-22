class employee:
    def __init__(self,name,Id,age):
        self.name = name 
        self.Id = Id
        self.age = age
    def get_details(self):
        print(f"Name : {self.name} \n Id : {self.Id} \n age : {self.age}m ")

class sde(employee): #inherit class empllyee ( all its attributers and methods)
    def __init__(self,name,Id,age,role):
        super().__init__(name,Id,age) # this is making to use the init fuction in parent class to declare the variables
        self.role=role
        
    def get_details(self):
        super().get_details()
        print(f"role : {self.role}")
        # print(f"Name : {self.name} \n Id : {self.Id} \n age : {self.age} \n role : {self.role}")

sel = sde("name",123,23,"sde")
sel.get_details()