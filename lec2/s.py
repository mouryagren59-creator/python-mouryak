l=[5,3,4,56,4,5,6,4,3,76,6,3,45]
big=max(l)
big2=l[0]
for i in l:
    if i>big2 and i<big:
        big2=i
print(big2)