import os 
a = os.listdir("dir")
print(a)                  #list the files present in directory

current_directory = os.getcwd()
print(current_directory)           # returns the current working directory

path_exist = os.path.exists("bhavesh.txt")     #Returns true if the file or dir exists
print(path_exist)

#os.remove("random.txt")     #Deletes the file

os.rmdir("dir")    #This function only removes empty directories. If the directory is not empty it will not rwmove the directory.