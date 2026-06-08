def rem(names , word):
    n = []
    for name in names:
        if not(name == word):
            n.append(name.strip(word))
            
    return n

l = ["Gagan123" , "Shona123" , "Demon123" , "Devil123"]
print(l)

remove = input("Enter the word you wanna strip and remove: ")

print(rem(l, remove))