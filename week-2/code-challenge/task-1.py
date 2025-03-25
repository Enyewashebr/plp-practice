# Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

numbers=int(input("Enter a number: "))
sum=0
for number in range(numbers):
    # number=int(input("Enter a number: "))
    sum+=number
print(sum)
