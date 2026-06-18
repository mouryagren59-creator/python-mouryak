text_file = "something.txt"
with open(text_file,"r") as f:
    data = f.read()
index=0
final=""
with open(text_file,"w") as f:
    for i in data:
        if data[index:index+len("nothing"):]=="nothing":
            final=data[:index:]+"something"+data[index+len("nothing")::]
            data=final
            index+=len("something")
        else :
            index+=1

    f.write(final)