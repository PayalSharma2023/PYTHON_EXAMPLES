#a list is a collection of things, enclosed in [ ] and separated by commas. The list is a sequence data type which is used to store the collection of data. A single list may contain DataTypes like Integers, Strings, as well as Objects. Lists are mutable, and hence, they can be altered even after their creation.
List = []
print("Blank List: ")
print(List)
#creating a list of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)
# Creating a List with the use of Numbers (Having duplicate values)
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of Numbers: ")
print(List)

# Creating a List with mixed type of values (Having numbers and strings)
List = [1, 2, 'Ritu', 4, 'For', 6, 'to']
print("\nList with the use of Mixed Values: ")
print(List)
print("Accessing a element from the list")
print(List[0])
print(List[2])
#creating a multi dimentional list (by nesting a list inside a list)
List = [[1,2,3], 4, "Goa", ["Patna",8]]
print("Accessing element from a multi-dimnsional list")
print(List[0][2])
print(List[3][0])
print("Accessing element using negative indexing")
# print the last element of list
print(List[-1])
# print the third last element of list
print(List[-3])

#Getting the size of python list
List1 = []
print(len(List1))
List2 = [10, 20, 14]
print(len(List2))
# Python program to take space separated input as a string split and store it to a list and print the string list input the list as string
string = input("Enter elements (Space-Separated): ")
# split the strings and store it to a list
lst = string.split() 
print('The list is:', lst) # printing the list
# input size of the list
n = int(input("Enter the size of list : "))
# store integers in a list using map, split and strip functions
lst = list(map(int, input("Enter the integer\
elements:").strip().split()))[:n]

# printing the list
print('The list is:', lst) 

# Reversing a list
mylist = [1, 2, 3, 4, 5, 'Geek', 'Python']
mylist.reverse()
print(mylist)
my_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(my_list))
print(reversed_list)


