try:
    a = int(input("enter an integer : "))
    b = int(input("enter an integer : "))
    c=a//b

except ZeroDivisionError:
    print("zero divisible has occured")
else:
    print("result 0f a//b is",c)
finally:
    print("Execution completed")