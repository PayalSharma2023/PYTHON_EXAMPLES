list2 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'b'] 
print(list2.count('b'))
list1 = [ ('Cat', 'Bat'), ('Sat', 'Cat'), ('Cat', 'Bat'),
		('Cat', 'Bat', 'Sat'), [1, 2], [1, 2, 3], [1, 2] ]

# Counts the number of times 'Cat' appears in list1
print(list1.count(('Cat', 'Bat')))

# Count the number of times sublist
# '[1, 2]' appears in list1
print(list1.count([1, 2]))
#List count() in Python raises TypeError when more than 1 parameter is passed.

# Python3 program to count the number of times
# an object appears in a list using count() method 

lst = ['Cat', 'Bat', 'Sat', 'Cat', 'Mat', 'Cat', 'Sat']

# To get the number of occurrences 
# of each item in a list
print ([ [l, lst.count(l)] for l in set(lst)])

# To get the number of occurrences 
# of each item in a dictionary
print (dict( (l, lst.count(l) ) for l in set(lst)))
