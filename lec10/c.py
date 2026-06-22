class employee:
    def __init__(self,name,age,Id):
        self.name = name
        self.age = age
        self.Id = Id
    def __str__(self):
        return f"Name : {self.name} \n age : {self.age} \n Id : {self.Id}"
class sde(employee):
    def __init__(self, name, age , Id ,role):
        super().__init__(name,age,Id)
        self.role = role
    def __str__(self):
        return super().__str__() + f"\nrole : {self.role}" 
        #this is called Dunder method means "double underscore" method 
class senior_sde(sde):
    def __init__(self, name, age, Id, role,level):
        super().__init__(name,age,Id,role)
        self.level = level
    def __str__(self):
        return super().__str__() + f"\nlevel :{self.level} "
    

# se1 = sde("name",234,14,"sde_1")
# #se1.get_details_1() is same as using that function in get_details_2
# print(se1)
senior_developer = senior_sde("cde",1234,25,"sde","100059")
print(senior_developer)