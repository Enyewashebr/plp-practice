# dictionery is a collection of key-value pairs
# dictionery is mutable
# dictionery is indexed with keys
# dictionery is ordered
# dictionery is changeable
# dictionery is allow duplicate values

# Create a dictionery
my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Access values in a dictionery
# print(my_dict[1]) # output: 30
print(my_dict['name']) # output: John
print(my_dict.get('age')) # output: 30
print(my_dict.keys()) # output: dict_keys(['name', 'age', 'city'])
print(my_dict.values()) # output: dict_values(['John', 30, 'New York']) 
