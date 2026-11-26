'''
Creating Python Variables 
Python has no commands for declaring variables 

A Variable is created the moment you first assign a value of it 
'''


x = 5 
y = "Jhon"

print(x)
print(y)

#Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 4 #x is of type int 
x = "Sally"  #x is now of type str 
print(x)

#Casting 
x = str(3) # x will be 3 
y = int('3') # y will be int 
z = float('3') # z will be float 

print(x,y,z)

#Get the type 

print(type(x))
print(type(y))
print(type(z))

"Single or Double Quotes"
#String variable can be declared either by using single or double quotes

x = "Jhon"
x = 'Jhon'

print(x)

"Case-sensitive"

a = 4
A = "Sally"
print(a)
#A will not overwrite a; 
