'''s = "hello world"  # Strings are immutable. Means string original value is not changeable.

a = len(s)
print(a)
#print(s.upper(), s)  here the new string is created HELLO WORLD BUT ",s" original value does not change which represents the immutability

print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())  '''

'''text = " Hello World "
print(text.strip())  # strip() functions remove the starting and ending whitespaces and new line.
print(text.lstrip())
print(text.rstrip())'''

text = "Python is fun an fun"
print(text.find("z"))  #This function will  return the index of the first occurence of the string.
print(text.index("is"))
print(text.replace("fun", "awesome")) #This function will replace the existing string with the new string

'''text = "Ashish,Bhavesh,Neha"
name = text.split(",")
print(name) # This function converts string into list.
new_text = "-".join(name) # The join() function takes a list of strings and joins them into a single string, using the specified separator.
print(new_text)'''

#Checking String Properties.   # These returns value in True or False.

'''text = "Python123"
print(text.isalpha())
print(text.isnumeric())
print(text.isalnum())
print(text.isspace())'''