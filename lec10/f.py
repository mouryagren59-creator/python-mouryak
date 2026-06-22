class A:
    def details(self):
        print("From Class A")
class B:
    def details(self):
        super().details()
        print("from class b")
class C(B,A):
    def details(self):
        super().details()
        print("from class c")

c1 = C()
print(C.__mro__)
# c1.details()
# c1.details()
c1.details()