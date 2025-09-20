age = int(input("Enter the age: "))
license = (input("Person is having driving license or not (True or False): "))
if license.lower() == "true":
    license = True
else:
    license = False
if(age >= 18):
    if license:
        print("You are allowed to drive.")
    else:
        print("You are not allowed to drive without license")
else:
    print("You are too young to drive.")