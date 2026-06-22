#gimme gimme gimme some time to think i'm in the bathroom looking at me face in the mirror is all i need 
#waiting until reaper takes my life never gonna get me out alive i will live a thousand million lives
#my patience is waning is this entertaining my patience is waning is this entertaining
#I I I got this feeling in my soul go ahead and throw your stones  
class member:
    def __init__(self,name,Id,age):
        self.name = name
        self.age = age
        self.Id = Id
    def __str__(self):
        return f"Name : {self.name} \n age : {self.age} \n Id : {self.Id}"
class student(member):
    def __init__(self, name, Id , age ,year ,school):
        super().__init__(name ,age   ,Id)
        self.year = year
        self.school = school
    def __str__(self):
        return super().__str__() + f"\nyear : {self.year} \n school : {self.school}" 
class staff(member):
    def __init__(self,name,Id,age,role):
        super().__init__(name,Id,age)
        self.role = role
    def __str__(self):
        return super().__str__() + f"role = {self.role}"
    
student_1 = student("abd",134,2519,"1st","scds")
print(student_1)
staff_1 = staff("dfg",125,25,"manager")
print(staff_1)

#polymorphism allows object of different types to be treated similarly. In other words , polymorphism allows objects to be treated as
#  single type of object, even if they are of differnt typies. this means that a single set of code can handle any object , even if
#  the object one of differnet types.xx