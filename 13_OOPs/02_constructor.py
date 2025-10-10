class Employee:
    def __init__(self, name, salary, bond):  #Initializing the object
        self.name = name      #Creating the instance attribute name salary and assign it with salary
        self.salary = salary
        self.bond = bond

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. The salary of {self.name} is {self.salary}. The bond of {self.name} is {self.bond}")
    
e1 = Employee("John Doe", 50000, 4)
print(e1.get_salary())
e1.get_info()
    