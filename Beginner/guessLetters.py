word = "evaporate"
wordArray = []
displayWordArray = []
usedLetters = []

for i in word:
    wordArray.append(i)
print(wordArray)

for i in range(len(word)):
    displayWordArray.append("_")
print(displayWordArray)

def checkLetterUsed(userInput):
    if userInput in usedLetters:
        prompt = "You've already used that letter."
    return prompt

def usedLettersToSet(usedLetters):
    print(set(usedLetters))

gameOn = True
while gameOn:
    userGuess = str(input("Enter a letter: "))
    usedLetters.append(userGuess)
    if userGuess in wordArray:
        while userGuess in wordArray:
            for i in range(len(wordArray)):
                if userGuess == wordArray[i]:
                    displayWordArray[i] = userGuess
            break
    else:
        usedLetters.append(userGuess)
        print("Letter not in word")
    
    print(displayWordArray)
    print(usedLetters)

    if displayWordArray == wordArray:
        print("You guessed the word!")
        gameOn = False

usedLettersToSet(usedLetters)