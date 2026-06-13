class person:
    def __init__(self,name,age,gender,height):
        self.name=name
        self.age=age
        self.gender=gender
        self.height=height

    def details(self):
        print(self.name,self.age,self.gender,self.height)
    def update(self):
        print("mourya")