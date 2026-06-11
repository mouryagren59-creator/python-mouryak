def change(xe):
    def g(ex):
        ex="table tennis"
        print(ex)
    xe=xe+1
    g(xe)
    return xe
x=4
print(x)
x=change(x)

print(x)
''' 
in the def it creates it own variables and doesn't depend on given pass by value variable
'''