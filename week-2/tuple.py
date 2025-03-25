# tuple is a collection of items in a particular order
# tuple is immutable
# tuple is indexed
# tuple is ordered
# tuple is changeable
# tuple is allow duplicate values    
# tuple is a collection of items in a particular order
letters=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print(letters)
print(letters[0]) # output: a
print(letters[-1]) # output: j
print(letters[2:5]) # output: ['c', 'd', 'e']
print(letters[:5]) # output: ['a', 'b', 'c', 'd', 'e']
print(letters[5:]) # output: ['f', 'g', 'h', 'i', 'j']
# tuple methods
print(len(letters)) # output: 10
print(letters.count('a')) # output: 1
print(letters.index('a')) # output: 0

