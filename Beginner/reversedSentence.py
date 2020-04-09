#Script that asks for a sentence from a user and returns it but in reversed.


s = 'This is a test sentence.'
userInput = str(input("Enter your sentence. Please enter a string with multiple words:"))

def reverseString(userString):

    a = userString.split(' ') # split the sentence
    strList = [elem for elem in a] #creating a list with sentence
    reverseList = strList[::-1] #reversed list
    reversedSentence = ' '.join([elem for elem in reverseList]) #reversedList turned into the reversed string
    return reversedSentence

print(reverseString(userInput))