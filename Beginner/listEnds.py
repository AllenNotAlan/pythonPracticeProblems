#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and 
#makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.


a = [1,2,3,4,5]

def listEnd(list):
    c = [num for num in list if num == list[0] or num == list[len(list)-1]]
    return c

print(listEnd(a))