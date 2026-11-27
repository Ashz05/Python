#in and not in are indentity operator

a = 5 
b = a 

print(a is b)
print(b is a) 
#because both pointing at the same memory location!
 
print(id(a))
print(id(b))
#140721172923304, 140721172923304

#let take datastructure 

a = ["apple","orange"]
b = a
print(a is b)
print(b is a)

#both point in the same memory location ('b' is point to the same reference location where 'a 'is pointing at)
#this is called shallow copy, thus whenever you make change in 'a', it will also reflect in 'b'

a.pop()
print(a)
print(b)

'''
Difference Between is and ==

    is - Checks if both variables point to the same object in memory
    == - Checks if the values of both variables are equal
'''

print(a == b) #it check the value of a and b 

