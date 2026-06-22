class employee:
    def __init__(self,name,age,Id):
        self.name = name
        self.age = age
        self.Id = Id
    def get_details_1(self):
        print(f"Name : {self.name} \n age : {self.age} \n Id : {self.Id}")
class sde(employee):
    def greet():
        print("hello world")
    # def __init__(self, name, age , Id ,role):en
        # super().__init__(name,age,Id)
        # sde.__init__(self,name,age,Id)
        # self.name=name
        # self.age=age
        # self.Id=Id

        self.role = role
    def get_details_2(self):
        self.get_details_1()
        print(f"role : {self.role}")

se1 = sde("name",234,14,"sde_1")
#se1.get_details_1() is same as using that function in get_details_2
se1.get_details_2()