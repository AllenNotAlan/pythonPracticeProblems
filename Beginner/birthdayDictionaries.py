def main():
    
    print("This is a dictionary. We know the birthdays of: ")
    print("Bianca, Allen and Tina")

    birthdayDict = {
        "Bianca": "13/08",
        "Tina": "22/01",
        "Allen": "27/04",
    }

    userInput = str(input("Enter the name of the person you want to know the birthday of:"))

    if userInput in birthdayDict:
        print("%s's birthday is %s" % (userInput, birthdayDict[userInput]))
    else:
        print("nah we don't have that person. Soz.")


if __name__ == "__main__":
    main()