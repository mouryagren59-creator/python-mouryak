def decorator2(add):
    def wrapper(a,b):
        print("started adding the two nubers")
        add(a,b)
        print("ended adding and answer is given")
    return wrapper

@decorator2
def add(a,b):
    print(f"the sum is {a+b}")
add(3,5)