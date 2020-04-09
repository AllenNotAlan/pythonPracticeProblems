#Given a list, create a new list without the duplicate elements of the list previously given.
a = [1,1,1,23,23,23,5,7,2343]

def removeDuplicates(list):
    a_without_duplicates = set(a)
    newList = []
    # newList = [elem for elem in a_without_duplicates] <- list comprehension. Much shorter solution
    for elem in a_without_duplicates:
        newList.append(elem)
    return newList

print(removeDuplicates(a))
