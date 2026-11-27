#assignment operators 


a = 5 # '=' is an assignment operator 

a += 5  # '+=' is an assignment operator adds the value from right side of the '='
print(a)

a -= 5 # '-=' is an assignment operators subtracts the value from left side of the '='
print(a)


#same wise "arithmetic operator + '=' operators combines assignment operator"
'+= -= *= /= **='

a **= 5
print(a)

a //=5
print(a)

#postfix and prefix 

'+= prefix =+ postfix'

'pre = pre-assignment {operator name}, post = post-assignement {operator name}'

#example 

a = 5
b = 1 

# b += a 
b =+ a
#as there are no a++ operator in python the a value doesn't increament by 1
print(a)
print(b)


#Walrus operator 
"The Walrus Operator"
"Python 3.8 introduced the := operator, known as the 'walrus operator'. It assigns values to variables as part of a larger expression:"

numbers = [1,2,3,4,5]

if(count := len(numbers)) > 3:
    print(f"List has {count} elements")


