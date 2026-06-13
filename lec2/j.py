def add():
    print("hwlloe")
class student:
    def __init__(self,name,id,cgpa):
        self.name=name  #(s2.name = )
        self.id=id
        self.cgpa=cgpa
        self.school="scds"
    def student_details(self):
        return f"Name: {self.name} id: {self.id} and CGPA :{self.cgpa}"
    def update_cgpa(self,new_gpa):
        self.cgpa=new_gpa
    def update_name(self,new_name):
        self.name=new_name
    def update_id(self,new_id):
        self.id=new_id
    def school_name(self):
        print(self.school)
        # user didn't gave the information about his school but the class defaultly makes his class as scds.

#what happened bala what are you doing

    #def compare(self,other):
        #print(other.name,self.name)

s1=student("mourya",21,7.4)
s2=student("xyz",100059,10)
print(s1.student_details())
s1.update_cgpa(8)
s1.update_name("sai mourya.k")
s1.update_id(100059)
print(s1.student_details())
#s1.compare(s2)
s1.school_name()