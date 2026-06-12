# import re

# with open("log.txt") as file:
#     text = file.read()

# word = "python"
# new_text = re.search(word , text , flags=re.IGNORECASE)
# print(new_text)
# start , end = new_text.span()
# print(text[start : end])


with open("log.txt") as file:
    lines = file.readlines()

    for line in lines:
        if "Python" in line:
            print(f"Yes, python is present")           