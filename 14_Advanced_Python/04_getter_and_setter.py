class Employee:
    def __init__(self, name, salary):
        self.name =  name
        self.salary = salary

    @property
    def first_name(self):
        l = self.name.split(" ")      # Getter
        #print(l)
        return l[0]
    @first_name.setter
    def first_name(self, first):
                l = self.name.split(" ")      # setter
                new_name = f"{first} {l[1]}"
                self.name = new_name

'''    @first_name.deleter
    def first_name(self):      
          del self.name'''

e = Employee("Jack Doe", 40000)
print(e.first_name)
e.first_name = "John"
print(e.name)
'''del e.first_name
print(e.name)   #Attribute Error'''

'''print(e.first_name())
e.set_first_name("John")
print(e.name)
'''



