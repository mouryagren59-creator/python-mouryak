s1=input("enter a string ")
d2={}
big_word=s1[1]
small_word=s1[1]
p=""
q=""
for i in s1:
    if i not in d2.keys():
        d2[i]=1
    else:
        d2[i]+=1

    if d2[i]==1:
        p=p+i
    elif d2[i]>1:
        q=q+i

print(f"{p}_{q}")
print(d2)