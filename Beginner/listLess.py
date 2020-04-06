
#Write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def printNumsLessThan(list):
    for nums in a:
        if nums < 5:
            print(nums)

#EXTRAS:
#Instead of printing the elements one by one, 
#make a new list that has all the elements less than 5 from this list in it and print out this new list.

def make_new_list(list):
    new_List =[]
    for nums in list:
        if nums < 5:
            new_List.append(nums)
    return new_List

#write this in one line of python? THIS IS CALLED LIST COMPREHENSION
print([x for x in a if x < 5])

#Ask the user for a number and return a list that contains only 
#elements from the original list a that are smaller than that number given by the user.
def listLessThan_userNum(list):
    userNum = int(input("Enter a number:"))
    new_List =[]
    for nums in list:
        if nums < userNum:
            new_List.append(nums)
    return new_List

# print(printNumsLessThan(a))
# print(make_new_list(a))
# print(listLessThan_userNum(a))
