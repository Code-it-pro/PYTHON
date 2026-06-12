with open("this.txt") as f:
    file1 = f.read()

with open("This_copy.txt") as f:
    file2 = f.read()

if file1 == file2:
    print("Both files are same!!")
else:
    print("Both files are not same!!")