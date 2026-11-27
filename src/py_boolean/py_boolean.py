#Boolean Values 

'''
In Programming you often need to know if an expression is True or False 
you can evaluate any expression in python, and get one of two answers, True or False 
unlike other programming languages : Python bool values is first letter of bool is capitalized (T or F), other programming language has small letters(true or false)
'''

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 10 
b = 91

if(a > b):
    print(True) 
else:
    print(False)


#Evaluate variables 

print("Value of String: ",bool("Hello")) 
print("Value of a Integer: ",bool(15))

#let's understand more about datatype bool values 

#if a string is empty (no values inside the string)

print("Value of a empty String: ",bool("")) #it produce False has there are no values in the string
print(bool("1")) #it should contain atleast one value to concule that it is an truthy value 

print("value of an Integer:1 ",bool(1)) #this is boolean of integer produce true has it a value unlike string, if the value is 0, it becomes false, negative numbers get true 
print("Value of an Integer:0 ",bool(0))
print("Value of an Integer:-1 ",bool(-1))

print("Value of a list: ")
#String, list, tuple, dictionary are all object(if there are 0 element in these datastructure then bool value will produce false)

#example 
#let's consider list data structure

element = [0] 
if(bool(element) == False):
    element.append(1)
else:
    element.pop()
print(element)


