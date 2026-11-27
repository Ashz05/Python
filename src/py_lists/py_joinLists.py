#Join two Lists
'''
There are several ways to join, or concatenate, two or more lists in python 
one of the easiest way by using the + operator 
'''

#Way - 1
list1 = ["a","b","c"]
list2 = [1,2,3]

list3 =list1 + list2 
print(list3)

#Way - 2 
list3 = [list1.extend(list2)]

#Way - 3 
list1 = ["a","b","c"]
list2 = [1,2,3]
list3 = [] 

for x in list1:
    # print(x)
    list3.append(x)

list3.extend(list2)
print(list3)