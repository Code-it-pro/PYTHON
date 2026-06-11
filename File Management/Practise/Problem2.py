# ROCK PAPER SCISSOR GAME
'''

SCISSOR PAPER STONE
user = ROCK + SCISSOR     1 + 3
user = PAPER + ROCK       2 + 1
user = SCISSOR + PAPER    3 + 2
computer = user ( DRAW )  ===>  same toh draw

REST ALL LOSE

'''

import random

handles = {
    1 : "ROCK",
    2 : "PAPER",
    3 : "SCISSOR"
}

def Updatescore(score):

    score_str = str(score)
    with open("Hi-score.txt","w+") as f:
        f.write(score_str)

def game(points, Lastbest):

    print("1. STONE\n2. PAPER\n3. SCISSORS")
    # Getting Inputs
    user = int(input("Enter your choice: \n"))

    if user not in [1, 2, 3]:
        print("Invalid Input\nChoose 1, 2, 3")
        # Restart the round with current points intact
        game(points, Lastbest)
        return

    computer = random.choice([1, 2, 3])
    
    # Displayinf your choices

    print(f'YOUR CHOICE {handles[user]}')
    print(f'COMPUTER CHOICE {handles[computer]}\n')

    # Game Logic
    if (user == computer):
        print("It a Draw!\n")
        score = points
        print("Score: ", score)
    elif (user == 1 and computer == 3):
        print("You Win!\n")
        points += 1
        score = points
        print("Score: ", score)
    elif (user == 2 and computer == 1):
        print("You Win!\n")
        points += 1
        score = points
        print("Score: ", score)
    elif (user == 3 and computer == 2):
        print("You Win!\n")
        points += 1
        score = points
        print("Score: ", score)
    else:
        print("You Lost\n")
        score = points
        print("Score: ", score)
    
    print("Current Score:", score)
    gamebest = score

    if gamebest > Lastbest:
        print(f"New Hiscore: {gamebest}")
        Lastbest = gamebest
        Updatescore(gamebest)
    
    print("\nPlay Again ? (yes/no)\nY - YES  ||  N - NO")
    retry = input("Choose (y / n): ")
    if retry.lower() == "y":
        print("")
        game(gamebest, Lastbest)
    elif retry.lower() == "n":
        if gamebest > Lastbest:
            Updatescore(gamebest)
        print(f"\nYour Final score: {gamebest}")
        print("Exiting Game........\n")
    else:
        print("Invalid Input\nExiting...\n\n")


print("WELCOME TO STONE PAPER AND SCISSORS")

points = 0
Lastbest = 0

with open("Hi-score.txt") as coin:
        line = coin.read()
if line != "":
    Lastbest = int(line)
else:
    Lastbest = 0

print(f"Your Last Best Score: {Lastbest}")
game(points, Lastbest)

print("Thanks for playing")