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

def game():

    print("1. STONE\n2. PAPER\n3. SCISSORS")
    # Getting Inputs
    user = int(input("Enter your choice: "))
    computer = random.choice([1, 2, 3])
    
    # Displayinf your choices
    print(f'YOUR CHOICE {handles[user]}')
    print(f'COMPUTER CHOICE {handles[computer]}\n')

    # Game Logic
    if user != 1 and user != 2 and user != 3:
        # Checking for valid inputs
        print("Invalid Input\nChoose 1, 2, 3")
    else:
        # main logic
        if (user == computer):
            print("It a Draw!")
        elif (user == 1 and computer == 3):
            print("You Win!")
        elif (user == 2 and computer == 1):
            print("You Win!")
        elif (user == 3 and computer == 2):
            print("You Win!")
        else:
            print("You Lost")
    
    print("Play Again ? (yes/no)\nY - YES  ||  N - NO")
    retry = input("Choose (y / n): ")
    if retry.lower() == "y":
        game()
    else:
        print("Exiting Game........")


print("WELCOME TO STONE PAPER AND SCISSORS")


game()

print("Thanks for playing")