import numpy

mylist = [[1,2,1],
          [2,2,1], 
          [2,1,2]]

def checkGrid(grid):
    for i in range(len(grid)):
        row = set([grid[i][0], grid[i][1], grid[i][2]])
        if len(row) == 1 and grid[i][0] != 0:
            return grid[i][0]

    for i in range(len(grid)):
        col = set([grid[0][i], grid[1][i], grid[2][i]])
        if len(col) == 1 and grid[0][i] != 0:
            return grid[0][i]

    diag1 = set([grid[0][0], grid[1][1], grid[2][2]])
    diag2 = set([grid[0][2], grid[1][1], grid[2][0]])

    if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
        return grid[1][1]

    return 0


# print(checkGrid(mylist))

#notes
# set() creates a set of numbers (duh). UNIQUE numbers. ie, if list = [1,1,2] then set(list) = {1,2} or if list =[1,1,1] then set(list) = {1}


# for i in mylist:
#     print (i)

# #check rows
# for x in range(len(mylist)):
#     if mylist [x][0] == mylist[x][1] and mylist [x][0] == mylist[x][2]:
#         print("There is a winner")
#     else:
#         print("No winner in row:",x)

# #check columns
# for y in range(len(mylist)):
#     if mylist[0][y] == mylist[1][y] and mylist[0][y] == mylist[2][y]:
#         print("There is a winner in column: ",y)
#         if mylist[0][y] == 1:
#             print("Player 1 wins")
#         else:
#             print("Player 2 wins")
#     else:
#         print("No winner in column:",y)

# #check diagonal
# # for x in range(len(mylist)-1):
# x = 0
# y = 0
# if mylist[x][y] == mylist[x+1][y+1]:
#     print("There is a winner in diagonal LEFT to RIGHT")
#     # print(mylist[x][y])
#     # if mylist[x][y] == 1:
#     #     print("Player 1 wins")
#     # else:
#     #     print("Player 2 wins")
# else:
#     print("NO winner in diagonal LEFT to RIGHT")