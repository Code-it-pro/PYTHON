# rename_me.txt ===> New_named.txt

import os

old_name = "rename_me.txt"
new_name = "New_named.txt"

os.rename( old_name , new_name)

print("file renamed successfully!")