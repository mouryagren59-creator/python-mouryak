def count_digits(num):
    num=abs(num) if num>0 else abs(num*-1)
    if num<10 and num>0:
        return 1
    else :
        return (count_digits(num//10)+1)
print("number of digits is",count_digits(-54321))