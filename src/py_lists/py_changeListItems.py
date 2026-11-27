#Python - Change List Items 

#Change item value 
#To change the value of a specific item, refer to the index number; 

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #change the value of the list 

print("apple Memory Location: ", id("apple")) #string have same memory location (case-sensitive)
for elem in thislist: #so in order to check any string that are present in the list we can use in(indetity operator)
    print(elem," memory Location: ",id(elem))

#Change the range of value 

thislist[1:3] = ["pineapple","strawberry"] #if the number of elements changed doesn't match with the slicing of the list will throw error 
print(thislist)

#Example :
thislist[1:5] = ["apple","cherry","pineapple","strawberry","cake"] #adds the element if the index number exeeds 
#but if the index number and the number of element which is changed or updated should be equal 
#Example: 
thislist = ["apple","cherry","pineapple","strawberry","cake"] 
thislist[0:3] = ["cherry"] #if there are less number of items mentioned it right-hand side then it will truncate the elements from the index range that you have mentioned!
print(thislist)

#insert() 
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:
thislist.insert(2,"watermelon")
print(thislist)