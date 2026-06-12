with open("this.txt") as f:
    copy = f.read()

with open("This_copy.txt" , "w" ) as f:
    f.write(copy + "\nI am Copyed!!")