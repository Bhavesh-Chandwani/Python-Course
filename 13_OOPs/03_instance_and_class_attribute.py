class Employee:
    company = "Dell"      #This is class attribute
    def __init__(self, name, salary, bond, company):  #Initializing the object
        self.name = name      #Create an the instance attribute name "name" and assign it with name
        self.salary = salary #Create an the instance attribute name "salary" and assign it with salary
        self.bond = bond #Create an the instance attribute name "bond" and assign it with bond
        self.company = company  #Create an the instance attribute name "comapny" and assign it with company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. The salary of {self.name} is {self.salary}. The bond of {self.name} is {self.bond}")
    
e1 = Employee("John Doe", 50000, 4, "Lenovo")
print(e1.get_salary())
e1.get_info()
print(e1.company)  # Lenovo because Instance attribute is present
print(Employee.company)  # Dell because class present

#Object Introspection
print(dir(e1))  #We can findout number of instances and methods are present in object.