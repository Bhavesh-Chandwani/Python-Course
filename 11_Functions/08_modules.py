'''
By using modules we can import the code or function which is written by others.
There are two types of modules.
1. Built in Modules
2. External modules
'''

import math
from urllib import response
import mymodule # Importing the module created by the user itself.
import requests

print(math.sqrt(29))
print(math.factorial(5))

mymodule.Hello()

response = requests.get("https://www.google.com")   # get is the function in whicn we can pass the url to get the html of the documents
print(response.status_code)

response = requests.get("https://api.github.com")
print(response.status_code)

response = requests.get("https://api.github.com")
print(response.headers)

response = requests.get("https://api.github.com")
print(response.json())