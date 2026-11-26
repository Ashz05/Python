#Built-in Data types 

'''
In Programming, data type is an important concept. 

Variables can store data of different types, and different types can do different things. 

Python has the following data types built-in by default, in these categories.

'''

#Setting up by constructor

x = str("Welcome to Python")
print(x)

x = int(20)
print(x)

x = float(20.5)
print(x)

x = list(("apple","orange","banana"))
print(x)

x = range(5)
print(x)

x = dict(name = "Jhon", age = 36)
print(x)

x = set(("apple", "banana" ,"cherry"))
print(x)

x = bool(5)
print(x)

x = bytes(5)
print(x)

x = bytearray(5)
print(x)

x = memoryview(bytes(x))
print(x)