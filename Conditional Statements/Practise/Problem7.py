post = "Software Engineer at Google with 5 years of experience in Python and JavaScript. Skilled in machine learning and data analysis. Gagandeep Singh is a passionate developer who loves to create innovative solutions to complex problems. He has a strong background in computer science and is always eager to learn new technologies."

Find = input("Enter a name to check if the post is talking about them: ")

# Check if the post contains the name "Gagandeep Singh"
if Find.lower() in post.lower():
    print(f"The post is talking about {Find}")
else:
    print(f"The post is not talking about {Find}")