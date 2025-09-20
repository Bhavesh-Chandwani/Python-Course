n = int(input("Enter the number: "))
i = 1
while i<=n:
    if i + 1 > n:
        print(i)
    else:
        print(i, end = ",")
    i+=1
print("Loop ends.")