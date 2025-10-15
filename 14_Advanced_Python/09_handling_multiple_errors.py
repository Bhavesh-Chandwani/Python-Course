while True:
    try:   
        a = int(input("Enter the  1st number: "))
        b = int(input("Enter the  2nd number: "))
        c = a / b
        print(c)
    except(ZeroDivisionError, ValueError)as e:
        print(f"An Error Occured: {e}")
'''    except ValueError:
        print("Please dont perform bad typecaste!")

    except ZeroDivisionError:
        print("Do  not Divide number by 0")

    except Exception as e:
        print("Some errors occured.", e)'''
