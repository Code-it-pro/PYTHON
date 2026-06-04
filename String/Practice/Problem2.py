name = input("What is your name? ")

Letter = '''
            Dear {name},
            You are Selected!
            {date}
        '''

print(Letter.replace("{name}", name).replace("{date}", "2024-06-30"))