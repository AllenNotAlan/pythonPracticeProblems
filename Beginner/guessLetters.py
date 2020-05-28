from pickword import pickWord

word = pickWord("sowpods.txt").lower()
wordArray = []
displayWordArray = []
usedLetters = set()
score = 6

def initialiseArrays(word, wordArray, displayWordArray):
    for i in word:
        wordArray.append(i)

    for i in range(len(word)):
        displayWordArray.append("_")

def checkLetterUsed(userInput,lettersUsedSet):
    if userInput in lettersUsedSet:
        print("You've already used that letter")

def checkLetterInWordArray(userInput, wordArray):
    if userInput in wordArray:
        while userInput in wordArray:
            for i in range(len(wordArray)):
                if userInput == wordArray[i]:
                    displayWordArray[i] = userInput
            break
    else:
        print("Letter not in word")
        global score
        score = score - 1


def printInfo(displayWordArray, lettersUsedSet):
    print(displayWordArray,"\n")
    print("Letters you've used:")
    print(lettersUsedSet)
    print("")

def printIntro():
    print("Welcome to hangman!\nWhat is this word:")

def main():
    printIntro()
    initialiseArrays(word, wordArray, displayWordArray)
    gameOn = True
    while gameOn:
        printInfo(displayWordArray, usedLetters)
        userGuess = str(input("Enter a letter: "))
        checkLetterUsed(userGuess, usedLetters)
        usedLetters.add(userGuess)
        checkLetterInWordArray(userGuess, wordArray)
        print(score)

        if score < 1:
            print("Game over")
            break

        if displayWordArray == wordArray:
            print("You guessed the word!")
            print("The word was: %s" % word.upper())
            gameOn = False

if __name__ == "__main__":
    main()