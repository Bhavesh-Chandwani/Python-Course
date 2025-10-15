while True:
    try:   
        a = int(input("Enter the  1st number: "))
        b = int(input("Enter the  2nd number: "))
        c = a / b
        print(c)

    except Exception as e:
        print("Some error occured", ",", e)