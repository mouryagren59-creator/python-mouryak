'''def words(str):
    w_v=0
    w_c=0
    for i in str :
        
        if (ord(i)==ord('a') or ord(i)==ord('e') or ord(i)==ord('i') or ord(i)==ord('o') or ord(i)==ord('u') ):
            w_v+=1
        elif (ord(i)<=ord('z') and ord(i)>=ord('a')):
            w_c+=1
    print(f"no of vowels is {w_v}")
    print(f"no of consonants is {w_c}")
words("mourya")'''

def words(str):
    str=str.lower()
    v=0
    c=0
    vowels='aeiou'
    for i in str :
        if i in vowels:
            v+=1
        elif i!=' ':
            c+=1
    print(v,c)
words('saiuniversity')