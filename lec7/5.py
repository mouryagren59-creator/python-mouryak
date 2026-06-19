def count(s):
    if s=="":
        return 0
    else :
        s=s[1::]
        return count(s)+1

s="tabletennis"
print(count(s))