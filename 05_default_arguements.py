def greet(name = "Guest"):
    return f"Hello, {name}"
print(greet())

#Eg 2
def details(name, age = 24):
    return f"Name : {name}, Age : {age}"
print (details("Bhavesh")) #  Age Default Value is Passed
print(details("Ashish", "16")) # Age is set to 16