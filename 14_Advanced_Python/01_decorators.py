#Decorator is a function that takes function as an arngument and returns new function (wrapper)with enhanced functionality.

def decorator(func):
    def wrapper():
        print(f"I'm about to execute this function.")
        func()
        print(f"This function is executed")
    return wrapper
@decorator
def say_hello():
    print("Hello!")
say_hello()

'''f = decorator(say_hello)
f()'''