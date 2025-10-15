def division(a, b):
    try:
        a = int(a)
        b = int(b)
        c = a / b
        print(c)
        return c
    except ValueError:
        print("Dont bad typecaste (enter numeric values)")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except Exception as e:
        print("Unexpected error:", e)
    finally:
        print("This finally block will always be executed")

a = input("Enter the 1st number: ")
b = input("Enter the 2nd number: ")
division(a, b)