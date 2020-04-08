#Same as previous listOverlap question but this time we have to use at least one list comprehension line

#Write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
#Make sure your program works on two lists of different sizes. Write this using at least one list comprehension.  


x = [1, 34, 55, 89]
y = [1, 12, 13, 23]

print(set(x))

combinedList = [i for i in set(x) if i in y]
print(combinedList)

result = []
for elem in combinedList:
    if elem not in result:
        result.append(elem)

print(result)