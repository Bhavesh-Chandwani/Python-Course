import shutil
#shutil.rmtree("dir")    #Deletes the entire directory even if it contains data.
#shutil.copy("bhavesh.txt", "ashish.txt")    #This method copy the data of existing file and paste it in another file which creates a new file
shutil.move("ashish.txt", "dir/")   #This method moves the file into another directory.