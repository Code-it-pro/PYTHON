f = open("poems.txt")

line = f.readline().lower()

while(line != ""):
    if("twinkle" in line):
        print(line)
    line = f.readline().lower()

f.close()