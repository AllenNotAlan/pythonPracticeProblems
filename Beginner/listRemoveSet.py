#Given a list, create a new list without the duplicate elements of the list previously given.
a = [1,1,1,23,23,23,5,7,2343]

def removeDuplicates(list):
    newList = set(a)
    return newList

print(removeDuplicates(a))
