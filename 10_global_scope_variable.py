x = 10     # Global Variable
def my_func():
    global x     # global keyword declared inside the local variable.
    x = 30       # global variable changed from 10 to 30
my_func()
print(x)         # output 30