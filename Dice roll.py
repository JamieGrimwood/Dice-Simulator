import random

def diceroll():
    # Roll a random number
    r= random.randint(1,6)
    print("Your number is: " + str(r))
    input("press ENTER to roll again")
    diceroll()

def start():
    print("Welcome to the Dice Roll Simulator Thingy")
    input("press ENTER to start")
    # Call the diceroll function
    diceroll()

# Start the program
start()
