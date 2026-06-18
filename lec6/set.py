s =set()
s1={0}
print(type(s))
print(type(s1))
l=[50,6,5,2,1,4]
for i in l[:]:
    s.add(i)
s.remove(4)
s.pop()
print(s)