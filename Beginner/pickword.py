from random import randint

listOfString = []
with open('sowpods.txt', 'r') as f:
    line = f.readline()

    while line:
        line = f.readline().strip()
        listOfString.append(line)
    
randomNum = randint(0,len(listOfString))
randomWord = listOfString[randomNum]

print("Picking random word...")
print(randomWord)