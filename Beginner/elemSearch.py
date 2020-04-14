#Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. 
#The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.


#elemSearch not binary?
def elemSearch(data, elem):
    dataLength = len(data)
    index = 0

    for i in range(dataLength):
        if data[i] == elem:
            index = i

    return index

def binarySearch(data, elem):

    data.sort()
    print(data)
    lower = 0
    upper = len(data) - 1

    while lower <= upper:
        
        middle = (upper + lower) // 2

        if data[middle] == elem:
            return middle
        elif data[middle] < elem:
            lower = middle + 1
        else:
            upper = middle - 1
    return -1


if __name__ == "__main__":

    l1 = [4,45,3,2,5]
    
    print(elemSearch(l1, 3))
    print(binarySearch(l1, 5))
