from random import randint

def pickWord(fileName):
    listOfString = []
    with open(fileName, 'r') as f:
        line = f.readline()

        while line:
            line = f.readline().strip()
            listOfString.append(line)
        
    randomNum = randint(0,len(listOfString))
    randomWord = listOfString[randomNum]

    print("Picking random word...")
    return randomWord