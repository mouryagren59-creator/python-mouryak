#print(chr(ord('S')-32))
a=int(input("enter an integer : "))
temp=a
count=0
add=0
while temp>0:
    r=temp%10
    temp=temp//10
    add+=r
    
print(add)
