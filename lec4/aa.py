def seperate(string):
    d1={}
    final=[]
    word=""
    for i in string:
        if i not in d1.keys():
            d1[i]=1
        else :
            d1[i]+=1
    for i in d1.keys():
        for j in range(d1[i]):
            word=word+i
        final.append(word)
        word=""
    print(final)

string=input("enter the string : ")
seperate(string)