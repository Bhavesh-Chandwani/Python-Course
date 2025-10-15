def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper
def exclaimed(func):
    def wrapper():
        return func() + "!!!"
    return wrapper
@uppercase
@exclaimed
def greet():
    return f"hello"
print(greet())



