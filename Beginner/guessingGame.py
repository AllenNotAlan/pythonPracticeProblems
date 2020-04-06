from random import randint

randomNum = randint(1,9)
print(randomNum)

attempts = 1
prompt1 = "What is your guess?:"
prompt2 = "Guess again:"
print("This is a number guessing game. Pick a number between 1-10. Enter 'exit' to leave game.")

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
    except ValueError:
        if userGuess =='':
            print("Invalid input. Please enter a correct value.")
            continue
        elif userGuess == 'exit':
            print("Exiting game")
            break