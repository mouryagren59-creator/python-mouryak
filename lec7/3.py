s="abcd"
try :
    i=int(input("enter the vlaue of the index"))
except(IndexError):
    print("over index use")

else:
    print(f"{s[i]}")
finally:
    print("execution is completed")

i=int(input("enter the value of the index"))
if i<len(s) and i>-1:
    print(f"{s[i]}")
else:
    print("over index use")