t=(11,2,9,4,0,6)
t=list(t)
# # small=min(t)
c=[]
while(len(t)>0):
    small=min(t)
    c.append(small)
    t.remove(small)
c=tuple(c)
print(c)
