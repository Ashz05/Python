# Python - Loop Lists

#Loop through a List 
thislist = ["apple","orange","pineapple"]
#By element in an list (this is like an enhanced for loop (called by other programming languages))
for element in thislist:
    print(element, end=" ")
print()

#Loop through the list by index number; 
print("Using for loop")
for index in range(len(thislist)):
    print(f"Index value {index} and the element is: {thislist[index]}")
    if index == len(thislist) - 1:
        print("end of the index")

#using while loop 
index = 0 
print("Using while Loop")
while index < len(thislist):
    print(thislist[index],end= " ")
    index += 1
print() 

#using list comprehension 

list_comprehension = [x for x in thislist]
print(list_comprehension)