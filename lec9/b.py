class animal:
    def sound(self):
        return "make sound"
    def walk(self):
        return "i can walk you dumbass"
    def eat(self):
        return "i can be carnivore or herbivore or omnivore"
    
class dog(animal): 
    #inherit the class animal
    #inherited class can use the main class functions
    #but the main class can't use the inherited class functions yohohohohohoho
    def sound_1(self):
        return "barks"
    def pet_1(self):
        return "it can be trained"
    def eat_1(self):
        return "it is carnivore"
    
class cat(animal):
    def sound_2(self):
        return "meow"
    def pet_2(self):
        return "it can be trained"
    def eat_2(self):
        return "it is carnivore"

a1 = animal()
print(a1.sound())

d1 = dog()
print(d1.sound_1())
print(d1.sound())
print(d1.walk())
print(d1.pet_1())
print(d1.eat_1())
c1 = cat()
print(c1.sound_2())
print(c1.pet_2())