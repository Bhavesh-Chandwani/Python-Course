'''f = open("bhavesh.txt", "r")
content = f.read()
print(content)
f.close()'''

def file_open(f):
    f = open(f, "r")
    content = f.read()
    print(content)
    f.close()
file_open("bhavesh.txt")
