l1 = list(map(int,input("enter the number ").split()))
big=l1[0]
small=l1[0]
for i in l1:
    if big<i:
        big=i
    if small>i:
        small=i
print(big,small)