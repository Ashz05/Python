'''
Escape Character
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
'''
# txt = "We are the so-called "Vikings" from the north"  -> Throws error 

txt = "We are the so-called \'Vikings\' from the north" #\""\ works for both single and double quotes 
print(txt)

txt = "We are the so-called \\ from the north" #to print a backslash 
print(txt)

txt = "We are the so-called \n\"Vikings\" from the north"
print(txt)