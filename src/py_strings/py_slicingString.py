#slicing 

'You can return a range of characters by using the slice syntax. '
'Specify the start index and the end index, separated by a colon, to return a part of the string'

b = "Hello world!"
print(b[:5])

"Slice to the end"
#By leaving out the end index, the range will go to the end:

print(b[2:])

'Negative indexing'

#use the negative indexes to start the slice from the end of the string!!

print(b[-5:-1])