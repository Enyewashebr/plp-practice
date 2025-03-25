




words= input("Enter a word: ").split()
list=words
# list.append(words)
new_list=[list[word] for word in range(1, len(list),2)]
print(list)
print(new_list)
