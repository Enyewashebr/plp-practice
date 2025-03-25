# Data structure in python
# List is a collection of items in a particular order
# List is mutable
# List is dynamic
# List is indexed
# List is ordered
# List is changeable
# List is allow duplicate values

# Create a list
my_list = [1, 2, 3, 4, 5]

# apply python list methods
my_list.append(6) # add an item to the end of the list
print(my_list) #output: [1, 2, 3, 4, 5, 6]
my_list.remove(2) # output: [1, 3, 4, 5, 6]
my_list.insert(2, 10) # insert an item at a specific index 
# output: [1, 3, 10, 4, 5, 6]
my_list[2] = 10 # change an item in the list       
print(my_list)
my_list.sort() # sort the list
print(my_list) # output: [1, 3, 4, 5, 6, 10]
my_list.reverse() # reverse the list
print(my_list) # output: [10, 6, 5, 4, 3, 1]
my_list.pop() # remove the last item from the list
print(my_list) # output: [10, 6, 5, 4, 3]
lsit =[1, 2, 3, 4, 5, 3, 2, 3]
# list.count(3) # count the number of times an item appears in the list
# print(list.count(3)) # output: 3


# list created by comprehension
my_lists = [x for x in range(1, 11)]

print(my_lists) # output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = ["number"*x for x in range(1, 6)]
print(numbers)
