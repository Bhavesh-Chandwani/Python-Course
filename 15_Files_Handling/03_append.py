#Append to a file called john doe. It should contain the basic data about the john doe.We are the hometown of John Doe

f = open('John Doe.txt', "a")
string = '''
He lives in Programming town 
'''
f.write(string)
f.close()