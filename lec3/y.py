d1={"A":["D","E"],"B":["E","C"],"C":["B"],"D":["A","E"],"E":["A","E","D"]}
key1,key2=input("enter the 2 keys ").split(" ")
mid=input("enter the middle key ")
if key1 and key2 in d1.keys():
    if key1 in d1[key2]:
        print("yes with first key")
    else :
        for i in d1[key2]:
            if key1 in d1[i]:
                print("yes but with second key ")
                print(f"it is connected with {i}")
                break
else :
    print("not correct keys ")