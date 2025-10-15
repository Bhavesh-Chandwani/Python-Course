def add_numbers(*numbers):
    print(f"The argumenst are of type {type(numbers)}")
    total = 0
    for num in numbers:
        total += num 
    return total

sum = add_numbers(1,2,3,4,5)
print(sum)