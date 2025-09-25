# Understanding the recursion with the example of Fibonacci series

# Fibonacci series is the sum of the 2 previous numbers usually starts with 0 and 1.

'''
0 1 1 2 3 5 8 13.....
0 1 2 3 4 5 6 7.....  # Indexes

fib (0) = 0
fib (1) = 1
fib (2) = fib(0) + fib(1)
fib (3) = fib(1) + fib(2)
fib (4) = fib(2) + fib(3)
fib (5) = fib(3) + fib(4)
fib (6) = fib(4) + fib(5)
fib (7) = fib(5) + fib(6)
fib(n) = fib(n-2) + fib(n-1)
'''

def fib(n):
    if n == 0 or n == 1:     # Base Case
        return n
    return fib(n-2) + fib(n-1)
print(fib(6))