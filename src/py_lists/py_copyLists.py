#Copy a List 
'''
You cannot copy a list simply by typing list2 = list1, 
because: list2 will only be a reference to list1 and the changes made in list1 will reflect in list2 
'''

thislist = ["apple","banana","pineapple"]
mylist = thislist
print(mylist)
print(thislist)

#this creates copy of reference location 
#you can check the memory location of both the list 

#------ Method - 1 -------
print()
print("Before using copy() method:")
print(id(thislist))
print(id(mylist)) #Both having same memory location, has 'mylist' is pointing to the same reference of the 'thislist'
print()
#inorder to make the variable point to different memory location, we need to use copy() method 
print("After using copy() method:")
mylist = thislist.copy() #returns a shallow copy 
print(id(mylist))
print(id(thislist))

#------ Method - 2 ------ 
# list() method
mylist = list(thislist)

print()
print("Before using list() method:")
mylist = thislist
print(id(thislist))
print(id(mylist)) #Both having same memory location, has 'mylist' is pointing to the same reference of the 'thislist'
print()
#inorder to make the variable point to different memory location, we need to use list() method 
print("After using list() method:")
mylist = list(thislist) #returns a shallow copy 
print(id(mylist))
print(id(thislist))


#------ Method - 3 ------
# [:] the slice operator 
print()
print("Before using slice operator:")
mylist = thislist
print(id(thislist))
print(id(mylist)) #Both having same memory location, has 'mylist' is pointing to the same reference of the 'thislist'
print()
#inorder to make the variable point to different memory location, we need to use slice operator
print("After using slice operator:")
mylist = list(thislist) #returns a shallow copy 
print(id(mylist))
print(id(thislist))