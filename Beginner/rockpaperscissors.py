#rock paper scissors game. Use while loops and break statements to fully implement

import time

rematch = True
while rematch != False:

    player1pick = str(input("Player One. Type rock, paper or scissors: "))
    player2pick = str(input("Player Two. Type rock, paper or scissors: "))

    if player1pick == 'paper' and player2pick == 'rock':
        print("Paper covers rock. Player 1 wins.")
    elif player1pick == 'rock' and player2pick == 'paper':
        print("Paper covers rock. Player 2 wins.")
    elif player1pick == 'paper' and player2pick == 'scissors':
        print("Scissors cuts paper. Player 2 wins.")
    elif player1pick == 'scissors' and player2pick == 'paper':
        print("Scissors cut paper. Player 1 wins.")
    elif player1pick == 'rock' and player2pick == 'scissors':
        print("rock breaks scissors. Player 1 wins.")
    elif player1pick == 'scissors' and player2pick == 'rock':
        print("rock breaks scissors. Player 2 wins.")
    else:
        print("Player1 picked {} and Player2 also picked {}! It's a draw!".format(player1pick,player2pick))

    playNewGame = str(input("Would you like to play another game? Y/N:"))
    if playNewGame == 'Y':
        print("Playing again! Resetting game...")
        time.sleep(2)
    elif playNewGame == 'N':
        print("Ending game. Thanks for playing!")
        break


