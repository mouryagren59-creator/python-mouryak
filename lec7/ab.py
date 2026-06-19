def multiple(m1,m2):
    if m2==1:
        return m1
    else :
        m2-=1
        return multiple(m1,m2)+m1
print(multiple(3,4))