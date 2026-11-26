#Python - String Concatenation 

"String Concatenation"
"To concatenate or combine, two strings you can use the + operator "

a = "1"
b = "2"


c = "a"
d = "b"

print(a + b) #note it is in string not an integer 
print(type(a + b)) #string 
#In order to convert into another type we can use int() constructor to type casting!
print(type(int(a + b))) #converted to integer datatype 

print(c + d)
print(type(c + d)) #can't use int for string datatype 
 
# print(int(c+d)) #produce value error : string can't be converted to 
