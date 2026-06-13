def len1(n):
    if isinstance(n,str):
        count=0
        for i in n:
            count+=1
        return f"length of string is {count}"
    elif isinstance(n,list):
        count1 = 0
        for i in n:
            count1+=1
        return f"length of list is {count1}"
    else:
        return "WRONG DATA STRUCTURE"
print(len1("mourya"))
print(len1([3,5,4,2,2,5]))
print(len1(432))