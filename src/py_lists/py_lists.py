#Python Lists

'''
List:
-----
Lists are used to stored multiple items in a single variable 
Lists are one of 4 built-in data types in python, used to store collections of data, the other 3 are Tuple, Set, and Dicitionary
Lists are created using square brackets'''

mylist = ["apple","banana","cherry"]
print(mylist)

#List items 
#List items are ordered, changeable and allow duplicate values 
#List items are indexed, the first time has index [0], the second item has index [1] etc. 

#Ordered 
#When we say that lists are ordered, it means that the items have defined order, and that order will not change.
#if you add new items to a list, the new items will be placed at the end of the lists.


#Changeable 
#The List is changeable, meaning that we can change, add , and remove items in a list after it has been cleared 

#Allow duplicates 
#Since list are indexed ,list can have items with the same value: 

thelist = ["apple","banana","cherry","apple","cherry"]
print(thelist)

#List length 
print(len(thelist))

#List items - Datatypes 
#List items can be of any datatype 

list1 = ["apple","banana","cherry",1,2,3,True,False,[],{},(),set()]

for elem in list1:
    print(type(elem))

#The list() constructor 
#It is also possible to use the list() constructor when creating a new list 

thislist = list(('apple','orange','cherry'))
print(thislist)