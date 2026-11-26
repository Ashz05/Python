"Global Variables"

'''
Variables that are created outside of a function (as in all of the examples in the previous page) are known as global variables 

Global variables can be used by everyone, both inside of functions and outside. 
'''

x = "Python"
#follows legb rule : { l : local, e : enclosing , g : global, b : built-in }
def func():
    y = " is Amazing!"
    print(x + y)

func()
