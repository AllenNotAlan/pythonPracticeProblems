#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

from datetime import date

userName = str(input("What is your name?"))
userAge = int(input("What is your age?"))

#current year (2020) as a variable
currentYear = date.today().year

#year born
birthYear = currentYear - userAge
turnHundred = birthYear + 100

print("Hi, {}. You are {} years old. You will turn 100 years old in {}.".format(userName, userAge, turnHundred))