#String format 

age = 36 
#this will produce an error:
# txt = "My Namee is Jhon, I am  " + age #Type error

'we can combine strings and number using f-strings or the format() method'

txt = "My name is Jhon, I'm {}".format(age)
print(txt)

'or'

txt = f"My name is Jhon, I'm {age}"
print(txt)

#placeholder and modifiers 

price = 59; 

txt = f"The price iss {price}$"
print(txt)

'''
A placeholder can include a modifier to format the value.
A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
'''

"Example"

pi = 3.1456723
print(f"{pi:.2f}")