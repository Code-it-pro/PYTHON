# this is appending files

text = "Hey I am a NEW text \n"

f = open("myfile.txt", "a")

f.write(text)

f.close()