# This is how we read files

f = open("file.txt", "r")
data = f.read()
print(data)
f.close()