#Python Number 
import random 

#int 
#float 
#complex

x = 1 
y = 2.8 
z = 1j 

exponential = 2e10  #Produces floating point number(integer)
x = 35e3 
y = 12E4 
print(x,y)

print(exponential)
print(x,y,z)
print(type(x))
print(type(y))
print(type(z))

rand = random.randint(1,2) #based on random integer from a to b (only provides random integer values not floating point values)
print(rand)


rand = random.random() #produces values between 0.0 to 1.0 (floating point precision)
print(rand)

rand = random.randrange(1,10) #integer values between a to b
print(rand)