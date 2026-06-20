# def details(name,age,school):
#     return f"name: {name}, age: {age}, school: {school}"
# print(details(name = "thanrun", age = 17, school ="scds"))
def details(**kargs):
    # for key,value in kargs.items():
    #     print(key,value)
    print(kargs)
details(name = "thanrun", age = 17, school ="scds", hobby = "coding", fav_food = "pizza")