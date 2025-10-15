'''a = int(input("Enter the  1st number: "))
b = int(input("Enter the  2nd number: "))
if b == 0:
    raise ValueError("Please dont divide number by 0")
c = a / b
print(c)'''

def check_age(age):
    if age < 18:
        raise ValueError("Age must be greater than 18")
    return "Access Granted!"
try:
    print(check_age(20))
    print(check_age(16))
except ValueError as e:
    print(f"Error : {e}")