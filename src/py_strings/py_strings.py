'''
Strings :  
---------

strings in python are surrounded by either single quotation marks, or double quotation marks 
'hello' is same as "hello"
you can display a string literal with the print() function 

''' 

print('Hello')
print("Hello")


#Quotes inside Quotes 

print("It's alright") 
print("He is called 'Jhonny'")


a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 


"String are Arrays"

'Like many other programming langauge, string in python are arrays of unicode characters'
'However python does not have a character data type, a single character is simply a string with a length of 1'

a = "Hello World"
print(a[1])


"Looping through string"

for i in a:
    print(i,end=" ")
print()


"String Length"

for i in range(len(a)): #gives you the index value of the len of the character
    print(a[i],end= "") , #end = " " will make it print horizontally instead of vertically 
print()

"Check string"

text = "The best things in life are free!"
print("free" in text) #returns bool values 

#Use if statement for you dedicated output
#Example 

if("free" in text):
    print("'free' is present in the text")
else:
    print("'free' not present in the text")