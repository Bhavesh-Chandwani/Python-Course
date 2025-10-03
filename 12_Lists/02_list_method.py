marks = [95,94,93,92,91,95]
marks_extension = [95,99,91]
#Till here the list is original 
print(marks)


#From here I have started performing operation with methods on lists and original list is going to change
marks.append(66)      #Adding new value at the end of the list
print(marks)  

marks.insert(1,96)    #Inserting the new value on the required index here "1" is index and "96" is the value we inserted on that index
print(marks)

marks.pop()  # This will remove the last value by default
print(marks)

marks.pop(1) #This will remove the value from the given index
print(marks)

marks.count(95)  # This Function will count the number of Occurence of value
print(marks.count(95))

marks.extend(marks_extension) # THis method will merge 2 lists
print(marks)

marks_3 = marks.copy()  #This method will copy the value of selected list.
print(marks_3)

marks.index(93)  #This method will tell the index of an element first occured.
print(marks.index(93))

marks.reverse()    #This method reverse the list
print(marks)

marks.sort()      #This method sort the list like chronological order
print(marks)

marks.remove(95) #This method removes the desired element which we do not require
print(marks)

marks.clear() # This method delete all the elements from the list
print(marks)

