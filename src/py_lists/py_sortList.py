#Sort List alphanumerically 

#Sort in ascending order 
thislist = ["orange","mango","kiwi","pineapple","banana"]
thislist.sort()
print(thislist)

#Sort in descending order
thislist.sort(reverse=True)
print(thislist)


def myfunc(n):
    return abs(n - 50)

thislist = [100,50,65,82,23]
thislist.sort(key=myfunc)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


#Reverse order 
'''
What if you want to reverse the order of a list, regardless of the alphabet 
the reverse() method reverses the current sorting order of the elements
'''

thislist.reverse()
print(thislist)