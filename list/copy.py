lis = ['Geeks','for','Geeks'] 
new_list = lis.copy() 
print('Copied List:', new_list)
# Initializing list 
lis1 = [ 1, 2, 3, 4 ] 
# Using copy() to create a shallow copy 
lis2 = lis1.copy() 

# Printing new list 
print ("The new list created is : " + str(lis2)) 

# Adding new element to new list 
lis2.append(5) 

# Printing lists after adding new element 
# No change in old list 
print("The new list after adding new element :" + str(lis2)) 
print ("The old list after adding new element to new list : \ " + str(lis1))
import copy 

# Initializing list 
list1 = [ 1, [2, 3] , 4 ] 
print("list 1 before modification:\n", list1) 

# all changes are reflected 
list2 = list1 

# shallow copy - changes to 
# nested list is reflected, 
# same as copy.copy(), slicing 

list3 = list1.copy() 

# deep copy - no change is reflected 
list4 = copy.deepcopy(list1) 

list1.append(5) 
list1[1][1] = 999

print("list 1 after modification:\n", list1) 
print("list 2 after modification:\n", list2) 
print("list 3 after modification:\n", list3) 
print("list 4 after modification:\n", list4)
#copy using slicing
list = [2,4,6] 
new_list = list[:] 
new_list.append('a') 
print('Old List:', list) 
print('New List:', new_list)
