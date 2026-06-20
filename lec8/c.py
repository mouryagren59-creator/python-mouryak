def added(*args):
    total = 0
    for i in args:
        total = total+ i
    return total

print("addition:", added(1.1,2,3,4,5))

