# a=int(input("enter a number : "))
 #for i in range(1,a+1):
  #  if(i%2==0 and i%3==0):
   #     print(i,end=" ")

a="Sai University"
a=a.lower()
count_v=0
count_c=0
for i in a:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count_v+=1
    elif (i!=' ') :
        count_c+=1
print(f"vowels = {count_v} and consonents = {count_c}")