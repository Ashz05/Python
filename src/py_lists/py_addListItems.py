#Python - Add List Items 

#append method - used to add element at the end of the lis t
thislist = ["apple", "banana", "cherry"]
thislist.append(["orange","pomo"]) #adds list inside the current list you are working on
# thislist.append("banana","kiwi") -> Throws error 
print(thislist)


#insert() 
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


#Extend() 
thislist = ["apple","banana","cherry"]
# thislist.extend("apple","orange") #same like append() only accept the iterable[str]
thislist.extend(["cherry","mango"]) #now the above .append(["item"]) works with the extend method  
#add element at the end of the list 
print(thislist)
