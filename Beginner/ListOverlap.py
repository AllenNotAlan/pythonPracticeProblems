from random import randint

#creates a random list of nums
randA = range(1, randint(1,100))
randB = range(1, randint(1,50))

#prints random numbers
print(randA)
print(randB)

#Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#and write a program that returns a list that contains only the elements that 
#are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.


#function that creates a new list and compares two lists' items. If there are common items they are stored in the new list
def joinLists(listA, listB):

    lengthA = len(listA)
    lengthB = len(listB)

    overLap = []
    if lengthA < lengthB or lengthA == lengthB:
        for nums in listA:
            i = 0
            while i < lengthB:
                if nums == listB[i]:
                    overLap.append(nums)
                i = i+1
    else:
        for nums in listB:
            i = 0
            while i < lengthA:
                if nums == listA[i]:
                    overLap.append(nums)
                i = i+1
    
    i = 0
    for nums in overLap:
        while i < len(overLap):                 # loops to cycle through new list and removes duplicates
            if nums == overLap[i]:
                overLap.remove(nums)
            i = i +1

    return overLap



def shorterEasierSolution(listA, listB):
    new_list = []
    for nums in listA:
        if nums in listB:
            if nums not in new_list:
                new_list.append(nums)
    return new_list


#printing solutions:::

# print(joinLists(randA,randB))
print(shorterEasierSolution(randA,randB))