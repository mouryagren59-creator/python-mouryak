class my_list :
    def __init__(self):
        self.l=[0,0,0,0,0,0,0,0]
        self.count = 0

    def my_append(self,value):
        self.l[self.count]=value
        self.count=self.count+1

    def print_list(self):
        print("[ ",end="")
        for i in range(self.count):
            print(self.l[i],end = ", ")
        print("]")

    def pop(self):
        self.l[self.count-1]=0
        self.count-=1

    def update_index(self,pindex,new_value):
        self.l[pindex]=new_value

    def delete_index(self,pindex):
        for i in range(pindex,self.count):
            self.l[i]=self.l[i+1]
        self.count-=1

    def delete_value(self,value):
        flag=0
        for i in range(0,self.count):
            if self.l[i]==value:
                for j in range(i,self.count):
                    self.l[j]=self.l[j+1]
                self.count-=1
                flag=1
                break
        if flag==0:
            print("element not found ")

    def insert(self,pindex,new_value):
        i=0
        for i in range(self.count, pindex-1,-1):
            self.l[i]=self.l[i-1]
        self.l[i]=new_value
        self.count+=1

l1=my_list()
l1.my_append(1)
l1.my_append(2)
l1.my_append(3)
l1.my_append(4)
l1.my_append(5)
l1.print_list()
l1.update_index(2,300)
print("after updating index 2 with 300")
l1.print_list()
l1.delete_value(1)
print("after deleting value one")
l1.print_list()
l1.insert(4,99)
print("after inserting 99 at fourth index")
l1.print_list()
l1.delete_index(1)
print("after deleating first index")
l1.print_list()