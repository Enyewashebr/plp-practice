# Sets in pyhton
# Set is a collection of unique items
# Set is mutable
# Set is dynamic
# Set is indexed
# Set is ordered
# Set is changeable
# Set is allow duplicate values

# Create a set
student_id = {6, 2, 3, 4, 5}

# Access values in a set
print(student_id.pop()) # 

# add an item to the set
student_id.add(1)
print(student_id) # output: {1, 2, 3, 4, 5, 6}

# remove an item from the set
# student_id.remove(2)
# print(student_id) # output: {1, 3, 4, 5, 6}

# clear the set
# student_id.clear()
# print(student_id) # output: set()   

# delete the set
# del student_id

# check if an item is in the set
print(1 in student_id) # output: False

# check if an item is not in the set
print(1 not in student_id) # output: True


set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.pop()) # output: 1
print(set1.pop()) # output: 1
print(set1.pop()) # output: 1
print(set1)
