
# userGuessCount = 0
# userCows = 0
# userBulls = 0

# randomNum = int(input("Enter a four digit number:"))
# randNumToList = []

# userGuess = int(input("Enter a guess:"))

#function make num into a list
def intoList(num):
    listNum = []
    i = 0
    while i < 4:
        x = num % 10
        newNum = (num - x)//10
        num = newNum
        listNum.insert(0,x)
        i = i + 1
    return listNum

def compareList(randList,userList):
    userCows = 0
    userBulls = 0
    randListLength = len(randList)
    userListLength = len(userList)

    for x in range(randListLength):
            if randList[x] == userList[x]:
                userCows = userCows + 1

    userBulls = randListLength - userCows

    print("{} cows, {} bulls".format(userCows,userBulls))

    return userCows
    
if __name__ == '__main__':
    randomNum = int(input("Enter a four digit number:"))
    randNumToList = intoList(randomNum)

    count = 0
    while True:
        userGuess = int(input("Enter your guess:"))
        userGuessToList = intoList(userGuess)

        userCows = compareList(randNumToList, userGuessToList)
        if userCows == 4:
            count = count + 1
            print("You guessed right! Game over! \nIt took you {} guesses.".format(count))
            break
        else:
            count = count + 1
            print("Number of guesses: {}".format(count))