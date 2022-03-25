# Import packages to extend Python (just like we extend VScode)
from random import randint
from tkinter import N

# re-import our game variables
from gameComponents import gameVars, winLose
 
# [] => this is an array
# name = [value1, value2, value3]
# an array is a special type of container that can hold multiples items
# arrays are indexed (their contents are assigned a number)
# the index always starts at 0
# define a win or lose function 
# player_choice == False
while gameVars.player_choice is False: 
    print ("===============*/RPS GAME */==================")
    print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
    print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
    print("===============================================")
    print("Choose your weapon! Or Type quit to exit\n") #\n means "new line"
    gameVars.player_choice = input("Choose rock, paper, or scissors: \n")

    if gameVars.player_choice == "quit":
        print("You choose to quit")
        exit ()

    print("user chose: " + gameVars.player_choice)

    # this will be the AI choice -> a random pick from the choices array
    gameVars.computer_choice = gameVars.choices[randint(0, 2)]

    print("computer chose: " + gameVars.computer_choice)

    if gameVars.computer_choice == gameVars.player_choice:
        print ("tie")

    elif gameVars.computer_choice == "rock":
        if gameVars.player_choice == "scissors":
            print ("you lose!")
            #verbose way
            # player_lives = player_lives -1
            #simplified way
            gameVars.player_lives -= 1
        else:
            print ("you win")
            gameVars.computer_lives -=1

    elif gameVars.computer_choice == "paper":
        if gameVars.player_choice == "scissors":
            print ("you win!")
            gameVars.computer_lives -= 1
        else:
            print("you lose!")
            gameVars.player_lives -= 1

    elif gameVars.computer_choice == "scissors":
        if gameVars.player_choice == "paper":
         print("you lose!")
         gameVars.player_lives -= 1
        else:
         print("you win")
        gameVars.computer_lives -= 1

    if gameVars.player_lives == 0:
        winLose.winorlose("lose")
        
    if gameVars.computer_lives == 0:
        winLose.winorlose("won")
       
    print ("Player lives:", gameVars.player_lives)
    print ("Computer lives", gameVars.computer_lives)

    # map the loop keep running, by setting player_choice back to False
    # unset, so that our loop condition will evaluate to True
    gameVars.player_choice = False
