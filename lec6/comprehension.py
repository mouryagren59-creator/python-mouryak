l = [i for i in range(1,6)]
print(l)
l1=[i*i for i in range(1,6)]
print(l1)
l2=[chr(i) for i in range(65,91)]
print(l2)
s="saiuniversity"
l3=[i for i in s]
print(l3)
d={i:i*i for i in range(1,9)}
print(d)
d1={chr(i) : i for i in range(65,75)}
print(d1)
d2=[i for i in range(1,20) if i%2==0]
print(d2)
s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
d3={ord(i):i for i in s if i not in "aeiouAEIOU"}
print(d3)