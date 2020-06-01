#modify part1 to load birthday dictionary from a JSON file, rather than having the dictionary defined in the program.
#BONUS: Ask the user for a name to add to the dictionary and update the JSON file.

import json

def menu():
    print("1.Get a Birthday\n2.Add a Birthday")
    userInput = int(input("What would you like to do: "))

    if userInput == 1:
        print("hello")
        getBirthday()
    elif userInput == 2:
        newName = str(input("Enter name:"))
        newBirthday = str(input("Enter birthay (dd/mm):"))
        writeToJson(newName, newBirthday)

def getBirthday():

    with open("birthdays.json", "r") as f:
        data = json.load(f)

    userInput = str(input("Enter the name of the person you want to know the birthday of:")).lower()

    if userInput in data:
        print("%s's birthday is %s" % (userInput, data[userInput]))
    else:
        print("nah we don't have that person. Soz.")

def writeToJson(name, birthday):

    newData = {
        name: birthday
    }

    with open("birthdays.json", "r+") as f:
        dataFile = json.load(f)
        dataFile.update(newData)
        f.seek(0) #resets the file pointer to 0
        json.dump(dataFile,f) #overwrite file with dict

def main():
    menu()

if __name__ == "__main__":
    main()