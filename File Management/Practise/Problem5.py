# Paragraph that it changes

# Are you actually stupid or something? 
# You're completely useless and literally ruin 
# everything you touch. No one cares about your dumb ideas 
# anyway. Just shut up and get lost, you total loser.

import re

words = ["stupid" , "useless" , "ruins" , "dumb"]

with open("not_normal_words.txt" , "r") as file:
    text = file.read()

print(text + "\n")

new_text = text

for v in words:
    new_text = re.sub(v , "#censored#", new_text , flags=re.IGNORECASE)

with open("not_normal_words.txt" , "w") as file:
    file.write(new_text)

print(new_text)