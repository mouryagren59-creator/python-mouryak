class animal:
    def sound(self):
        print("animal makes sound")
class dog(animal):
    def sound(self):
        print("dog barks")
class cat(animal):
    # pass
    def sound(self):
        print("cat purs")
d1 = dog()
d1.sound()
c1 = cat()
c1.sound()