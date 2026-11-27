#Python - Remove List items 

#Remove Specified items
#The remove() method removes the specified item. 

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") #supports only str value, no element found throws error 
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(int("1")) #supports only index value 
print(thislist)

#if you don't specify any index in pop() function then it will remove the last element in an list 
thislist.pop()
print(thislist)

#The del keyword also removes the specified index 

thelist = ["apple","banana","cherry"]
del thelist[0]
print(thelist)

#Clear the list 
#the clear() method empties the list 

thislist = ["apple","banana","cherry"]
thislist.clear()
print(thislist)