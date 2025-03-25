# Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.


name=input("Enter your name: ")
age=input("Enter your age: ")
favorite_color=input("Enter your favorite color: ")
person={"name":name, "age":age, "favorite_color":favorite_color}
print(person)
