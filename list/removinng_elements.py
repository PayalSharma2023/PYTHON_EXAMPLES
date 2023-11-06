# Python program to demonstrate
# Removal of elements in a List

# Creating a List
List = [1, 2, 3, 4, 5, 6,
		7, 8, 9, 10, 11, 12]
print("Initial List: ")
print(List)

# Removing elements from List
# using Remove() method
List.remove(5)
List.remove(6)
print("\nList after Removal of two elements: ")
print(List)
# Creating a List
List = [1, 2, 3, 4, 5, 6,
		7, 8, 9, 10, 11, 12]
# Removing elements from List
# using iterator method
for i in range(1, 5):
	List.remove(i)
print("\nList after Removing a range of elements: ")
print(List)
List = [1, 2, 3, 4, 5]

# Removing element from the
# Set using the pop() method
List.pop()
print("\nList after popping an element: ")
print(List)

# Removing element at a
# specific location from the
# Set using the pop() method
List.pop(2)
print("\nList after popping a specific element: ")
print(List)
# Python program to demonstrate
# Removal of elements in a List

# Python code to demonstrate the working of 
# del and pop() 

# initializing list 
lis = [2, 1, 3, 5, 4, 3, 8] 

# using del to delete elements from pos. 2 to 5 
# deletes 3,5,4 
del lis[2 : 5] 

# displaying list after deleting 
print ("List elements after deleting are : ",end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 
	
print("\r") 

# using pop() to delete element at pos 2 
# deletes 3 
lis.pop(2) 

# displaying list after popping 
print ("List elements after popping are : ", end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 
# Python code to demonstrate the working of 
# sort() and reverse() 

# initializing list 
lis = [2, 1, 3, 5, 3, 8] 

# using sort() to sort the list 
lis.sort() 

# displaying list after sorting 
print ("List elements after sorting are : ", end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 
	
print("\r") 

# using reverse() to reverse the list 
lis.reverse() 

# displaying list after reversing 
print ("List elements after reversing are : ", end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 
# Python code to demonstrate the working of 
# extend() and clear() 

# initializing list 1 
lis1 = [2, 1, 3, 5] 

# initializing list 1 
lis2 = [6, 4, 3] 

# using extend() to add elements of lis2 in lis1 
lis1.extend(lis2) 

# displaying list after sorting 
print ("List elements after extending are : ", end="") 
for i in range(0, len(lis1)): 
	print(lis1[i], end=" ") 
	
print ("\r") 

# using clear() to delete all lis1 contents 
lis1.clear() 

# displaying list after clearing 
print ("List elements after clearing are : ", end="") 
for i in range(0, len(lis1)): 
	print(lis1[i], end=" ") 
