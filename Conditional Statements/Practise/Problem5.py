names = ["Alice", "Bob", "Charlie", "David", "Eve"]

name = input("Enter a name: ")

if name in names:
    print(f"{name} is in the list.")
else:
    print(f"{name} is not in the list.")