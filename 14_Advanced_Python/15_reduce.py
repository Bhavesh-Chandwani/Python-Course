from functools import reduce
numbers = [1,2,3,4,5,6,7]
def sum(a,b):
    return a + b
new_num = reduce(sum, numbers)
print(new_num)