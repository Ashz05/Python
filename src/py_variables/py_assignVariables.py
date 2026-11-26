'''
Many values to multiple variables 

Python allows you to assign values to multiple variables in one line: 
''' 

x,y,z = "Orange", "Banana", "Cherry"
print(x,y,z)

#One value to Multiple variables 

x = y = z = "Orange"

x ="Banana"
print(x)
print(y)
print(z)

'Unpack a Colletion'
"if you have collection of values in a list, tuple, etc. Python allows you to extract the values into variables. This is called Unpacking"

fruits = ["Apple","Orange","Pineapple"]
x,y,z = fruits
print(x,y,z)