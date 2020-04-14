from random import randint
import time

randomNum = randint(1,9)
print(randomNum)

attempts = 1
prompt1 = "What is your guess?:"
prompt2 = "Guess again:"
print("This is a number guessing game. Pick a number between 1-10. Enter 'exit' to leave game.")

err = "Negative Number. Invalid input."

while True:
    userGuess = input(prompt1)
    try:
        guess = int(userGuess)
        if guess > randomNum:
            print("Too high")
            attempts = attempts+1
        elif guess < randomNum:
            print("Too low")
            attempts = attempts+1
        elif guess == " ":
            print("Please enter a number.")
            continue
        else:
            print("That's correct")
            print("{} attempts until you got it right!".format(attempts))
            break
    except ValueError as err:
        if userGuess =='':
            print(err)
            continue
        elif userGuess == 'exit':
            print("You chose to exit the game. Leaving game in \n...")
            for x in range(3,0,-1):
                time.sleep(1)
                print("...{}".format(x))
            time.sleep(1)
            print("You have left the game.")
            break