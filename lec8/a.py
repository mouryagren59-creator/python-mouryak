def decorator1(greet):
    def wrapper():
        print("started the greeting")
        greet()
        print("ended the greeting")
    return wrapper
@decorator1
def greet():
    print("namaskaram !")

greet()