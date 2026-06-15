s1=input("enter a string ")
d2={}
big_word=s1[1]
small_word=s1[1]
d2[big_word]=0
d2[small_word]=0

for i in s1:
    if i not in d2.keys():
        d2[i]=1
    else :
        d2[i]+=1
    if d2[big_word]<d2[i]:
        big_word=i
    elif d2[small_word]>d2[i]:
        small_word=i
print(f"most counted word is {big_word}")
print(f"least counted word is {small_word}")
