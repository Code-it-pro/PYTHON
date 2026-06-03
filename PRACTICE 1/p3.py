import os

# Use '.' to represent the current directory where the script is saved
directory_path = 'C:/Games' 

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)