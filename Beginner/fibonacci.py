#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
#Take this opportunity to think about how you can use functions. 
#Make sure to ask the user to enter the number of numbers in the sequence to generate.

#Hint:The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
#The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …

userInput = int(input("How many fibonnaci numbers to generate:"))

def fib(num):
    x = 0
    y = 1

    i = 0
    while i < num:

        z = x + y
        x = y
        y = z

        i = i + 1
        print(x)


fib(userInput)