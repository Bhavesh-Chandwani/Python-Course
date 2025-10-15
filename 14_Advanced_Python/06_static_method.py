#from math import factorial   Ins tead of Mathutil we can import math module.
class MathUtils:
    @staticmethod
    def factorial(n):
       if n == 0 or n == 1 :
           return 1
       else:
           return n *MathUtils.factorial(n-1)
m = MathUtils()
print(m.factorial(5))
        