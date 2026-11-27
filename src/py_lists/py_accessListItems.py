#Access List items 

'''
Access items :
List items are indexed and you can access them by referring to the index number 
'''

thislist = ["apple","banana","cherry"]
print(thislist[1])

#Negative indexing 
print(thislist[-1])

#Range of indexes 
#You can specify a range of indexes by specifying where to start and where to end the range 

thislist = ["banana", "cherry", "orange", "kiwi", "melon", "mango",""]
print(thislist[4:])
print(thislist[:4])

#Check if the item exists 
result = ""
for index in range(len(thislist)):
    if bool(thislist[index]) == False:
        result = f"There is Empty Value Present in the List found at index : {index}"
    else:
        result = "There is No Empty Value Present in the List"
print(result)

