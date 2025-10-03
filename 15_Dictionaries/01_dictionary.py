student = {"name" : "John", "age" : 22, "gender" : "Male,", "city" : "Mumbai"}
print(student)

#Accessing Values
print(student["name"])  #John

#Modifying Values
student["age"] = 24
print(student)

#Adding New Key Value Pair
student["city_2"] = "New Delhi"
print(student)