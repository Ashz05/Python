# Python  - Modify Strings 

#Python has set of built-in methods that you can use on strings 
"Uppercase" 

a = "Hello world!"
print(a.upper()) #upper() function used to make all the characters in the string to upper case 

#Note : these function doesn't change the original string, you need to initalise another variable to make the change visible (as string are immutable(can't change the value!))

print(a.lower())

a = " Hello, World! "
print(a) #as you can see there are unwanted whitespaces in the above string 
#in order to remove the string white spaces we can use string in built function called strip() function 
print(a.strip()) #Now you can see there are no white spaces 

"Replace string" 
'The replace() method replaces string with another string'

a = "Hello world!"
print("Memory location of a: ",id(a)) #Previous memory location!
a = a.replace("H","T")
print("Memory location of a: ",id(a)) #current meemory location!
print(a) #in order to make changess we need to assign the varible 
# (Note: the Hello world is not really replace, the variable a is now pointing to another memory location)

"Split String"
#The split() method returns a list where the text between the specified separator become the list items

a = "Hello, World!" 
print(a.split(","))# returns the list of values, remove the character which have mentioned in the method!

