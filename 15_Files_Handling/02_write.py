#Write to a file called john doe. It should contain the basic data about the john doe

f = open('John Doe.txt', "w")
string = '''
The John Doe is the non existential character who lives is programming world
In every programming language his name is always used
'''
f.write(string)
f.close()