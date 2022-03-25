from random import randint
from tkinter import N
# re-import our game variables

from gameComponents import gameVars


def winorlose (status):
    if status == "won!":
        pre_message = "You are the Winner!"
    else:
        pre_message= "You lose!"

    print(pre_message + "! Would you like to play again?")
    choice = input("Y / N? ") 

    if choice == "N" or choice == "n":
        print ("You choose to quit! Better luck next time!")
        exit()
    elif choice == "Y" or choice == "y":
        #reset the player lives and computer lives
        #and reset player choice to False, so our loop restarts
        gameVars.playerlives = gameVars.total_lives
        gameVars.computer_lives = gameVars.total_lives
        gameVars.player_choice = False
    else:
        print("make a valid choice -Y or N")
        #this might generate a bug that we need to fix later
        choice = input("Y / N? ")