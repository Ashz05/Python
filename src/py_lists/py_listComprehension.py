'''
List Comprehension:
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:
Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
Without list comprehension you will have to write a for statement with a conditional test inside
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#without list-comprehension 

new_fruits = [] 

limit = 0 
for fruit in fruits:
    if limit <= 3:
        limit += 1 
        new_fruits.append(fruit)
    else: 
        print("Limit Reached!")
        break
print(new_fruits)

#using list comprehension 

new_fruits = [fruits[x] for x in range(len(fruit)-1)]
print(new_fruits) #same addition of element but in much simpler way to write the code. 

#this is the reason why we use list comprehension!
#Syntax for list comprehension 
'''
newlist = [expression for item in iterable if condition == True]
'''

#iterable : 
'''
The iterable can be any iterable object, like a list, tuple, set, etc..
'''

newlist = [x for x in range(5)]
print(newlist)

#with if conditionals 
newlist = [x for x in range(10) if x <= 5]
print(newlist)

#Expression: 
#The Expression is the current item in the iteration, but it aslo the outcome, which you can manipulate before it ends up like a list item in the new list: 

newlist = [x.upper() for x in fruits]
print(newlist)