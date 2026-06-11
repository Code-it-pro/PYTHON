# Reading Multiple lines

f = open("myfile.txt")

# Line1 = f.readline()
# print(Line1 , type(Line1))

# Line2 = f.readline()
# print(Line2 , type(Line2))

# Line3 = f.readline()
# print(Line3 , type(Line3))

# Using while

Line = f.readline()

while (Line != ""):
    print(Line)
    Line = f.readline()

f.close()