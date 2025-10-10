class Dog:
    def __init__(self, name, breed, age):
        self.name = name #public member
        self._breed = breed #protected member
        self.__age = age #private member

    #Public Method
    def get_info(self):
        return f"Name : {self.name}, Breed : {self._breed}, :Age :{self.__age}"
    
    #Getter and Setter for Private attribute
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print(f"Invalid Age!")
d = Dog("Rambo", "German Shepherd", 10)
print(d.name)    # Accessing public member
print(d._breed)  # Accessing protected member
print(d.get_age()) # Accessing private member using getter

#Modifying private member using setter
d.set_age(12)
print(d.get_info())