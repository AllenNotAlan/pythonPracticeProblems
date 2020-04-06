# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)
############################


#TEST
# flip a list:

# a = [1,2,3,4,5]
# b = []

# i = len(a)-1
# while i > -1:
#     b.append(a[i])
#     i = i-1

# print(b)

print("This will detect whether a word is a palindrome or not.")
prompt = str(input('Please enter a word:'))

def palindromeTest(userWord):
    new_Word = []
    wordAsList = list(userWord)
    userWordStr = ''.join(wordAsList)
    print(userWordStr)

    i = len(wordAsList) - 1
    while i > -1:
        new_Word.append(wordAsList[i])
        i = i-1
    new_ListasString = ''.join(new_Word)
    print(new_ListasString)
    if userWordStr != new_ListasString:
        print("not palindrome")
    else:
        print("palindrome")

    # if str(wordAsList) == str(newWordAsList):
    #     print("True")
    # else:
    #     print("False")

palindromeTest(prompt)

###########