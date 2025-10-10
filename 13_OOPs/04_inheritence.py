class Animal:          # Super Class or Parent class
    def __init__(self, name, age):
        self.name = name
        self. age = age
    def speak(self):
        print (f"{self.name} speaks", end = "")
        
#Single Inheritence
class Dog(Animal):    
    def speak(self):
        super().speak()    #super keyword() allows us to call the method and functions from parent class instead of completely ovverriding it.
        print(f" Woof")

#Multilevel Inheritence
class Breed(Dog):   
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def show_breed(self):
        print(f"{self.name} belongs to {self.breed}")

#Multiple Inheritence..
class Friendly:
    def nature(self):
        print(f"{self.name} is Friendly")

class Golden_Retriever(Dog, Friendly):
    def speak(self):
        super().speak()

#Create Objects   
dog1 = Dog("Rani", 5)
print(dog1.name)
print(dog1.age)
dog1.speak()

dog2 = Breed("Bruno", 4, "Labrador")
print(dog2.name)
print(dog2.age)
dog2.show_breed()

dog3 = Golden_Retriever("Judy", "6")
print(dog3.name)
dog3.nature()
dog3.speak()