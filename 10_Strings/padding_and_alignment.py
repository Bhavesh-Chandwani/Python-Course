'''text = "Bhavesh"
print(f"{text:>10}")
print(f"{text:<10}")
print(f"{text:^10}")'''

#Padding
'''s = "Bhavesh"
print(f"{s:10}") # Default padding (Left Side)
print(f"{s:>10}")
print(f"{s:^10}")
'''
#Custom Padding Character
'''s = "Bhavesh"
print(f"{s:*<10}")
print(f"{s:*>10}")
print(f"{s:*^15}")'''

#Alignment without f strings
s = "Python"
print(s.ljust(10, "-"))
print(s.rjust(10, "-"))
print(s.center(10,"-"))