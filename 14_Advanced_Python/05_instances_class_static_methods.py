class Employee:
    company = "Dell"

    #Instance Method
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def print_info(self):
        print(f"The name of the employee : {self.name}. Salary : {self.salary}")

    #Static Methods
    @staticmethod
    def calc(a,b):
        return a + b
    
    #Class Methods.
    @classmethod
    def print_company(cls,):
        print(cls.company)
        
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = Employee("John Doe", 35000)
e1.print_info()
#print(Employee.company)
print(e1.calc(5,8))
e1.print_company()
e1.change_company("Acer")
e1.print_company()