#Class - Is the template or Blueprint.
#Object - Specific instance created from the the template (class).

class Employee:
    company = "Hp"

    def get_salary(self):           # self is important it is refers to the object of the class which is being created 
        return 34000
    
e1 = Employee()
print(e1.get_salary())
print(e1.company)    