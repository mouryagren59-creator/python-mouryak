d1={"A":["D","E"],"B":["E","C"],"C":["B"],"D":["A","E"],"E":["A","E","D"]}
key1,key2=input("enter the 2 keys ").split(" ")
mid=input("enter the middle key ")
if key1 and key2 in d1.keys():
    if key1 in d1[mid] and mid in d1[key2]:
        print("yes")
    else :
        print("no")
else:
    print("not correct keys")


