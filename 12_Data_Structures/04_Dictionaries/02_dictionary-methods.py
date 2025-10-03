student = {"name" : "John", "age" : 22, "gender" : "Male", "city" : "Mumbai"}
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
student.update({"age" : 24, "city" : "New Delhi"})
print(student)

#Iterating Dictionaries
for key in student:
    print(key, ":", student[key])

student.pop("city")
print(student)

student.clear()
print(student)

#Nesting Dictionaries


'''dict = { 101: {"name" : "John", "age" : 22, "gender" : "Male", "city" : "Mumbai"},
     102: {"name" : "Jane", "age" : 25, "gender" : "Female", "city" : "NYC"} }
print (dict[101]["age"])
'''
