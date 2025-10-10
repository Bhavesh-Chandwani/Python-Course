from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass     # Abstract method no implementation here

    def display_name(self):
        print(f"{self.__class__.__name__} : {self.name}")   #Concrete Method

class Dog(Animal):
    def make_sound(self):
        print(f"Dog Woofs")

class Cat(Animal):
    def make_sound(self):
        print(f"Cat Meows")

dog = Dog("Kite")
dog.display_name()
dog.make_sound()

cat = Cat("Pretty")
cat.display_name()
cat.make_sound()