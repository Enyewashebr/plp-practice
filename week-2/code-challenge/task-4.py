# Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
set1=set(input("Enter a number: "))
set2=set(input("Enter a number: "))
set3=set1.intersection(set2)
print(set3)
