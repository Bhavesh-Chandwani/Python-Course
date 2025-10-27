import requests

r = requests.get('https://api.github.com/users/Bhavesh-Chandwani')

with open("Bhavesh-Chandwani.txt", "w") as f:
    f.write(r.text)