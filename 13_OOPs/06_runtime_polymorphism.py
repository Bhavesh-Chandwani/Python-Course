#1. Method Overriding
# We start with a base class and then a subclass that "overrides" the speak method.
class Animal:
    def speak(self):
        return f"The Generic Sound."
class Dog(Animal):
    def speak(self):
        return "Woof"
print(Dog().speak())

#2. Duck Typing
class Cat(Animal):
    def speak(self):
        return "Meow"

def make_animal_speak(animal):
# This function works for both Dog and Cat because they both have a 'speak' method.
    return animal.speak()
print(make_animal_speak(Dog()))
print(make_animal_speak(Cat()))

#3.Operator Overloading 
# We create a simple class that customizes the '+' operator
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def print_vector(self):
        print(f"X is {self.x}, Y is {self.y}")
v1 = Vector(3,5)
v2 = Vector(7,3)
v3 = v1 + v2
v3.print_vector()