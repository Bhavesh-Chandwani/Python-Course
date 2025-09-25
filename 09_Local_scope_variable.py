x = 10           # global Variable
def func():
    x = 5        # local variable   
    print(x)     #  output =  5
func()
print(x)         # output = 10  Global Variable x remains unchanged.