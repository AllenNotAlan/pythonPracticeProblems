from checkTicTacToe import checkGrid
grid = [[0,0,0],
        [0,0,0],
        [0,0,0]]

# grid = [['X','X','X'],
#         ['X','X','X'],
#         ['X','X','X']]

# #DRAW O > X
# grid = [['O','O','X'],
#         ['X','O','O'],
#         ['O','X','X']]

# #DRAW O < X
# grid = [['O','X','X'],
#         ['X','O','O'],
#         ['O','X','X']]

elapsed_turns = 0

def inputCoor1(grid):
    x, y = input("Player 1 enter two numbers: ").split()
    x, y = [int(x), int(y)]
    if grid[x][y] != 0:
        print("Already occupied")
        inputCoor1(grid)
    else:
        grid[x][y] = "X"
        global elapsed_turns
        elapsed_turns = elapsed_turns + 1
    # printGrid(grid)

def inputCoor2(grid):
    x, y = input("Player 2 enter two numbers: ").split()
    x, y = [int(x), int(y)]
    if grid[x][y] != 0:
        print("Already occupied")
        inputCoor2(grid)
    else:
        grid[x][y] = "O"
        global elapsed_turns
        elapsed_turns = elapsed_turns + 1
    # printGrid(grid)

def printGrid(grid):
    for i in range(len(grid)):
        print(grid[i])

# def checkGrid(grid):
#     for i in range(len(grid)):
#         row = set([grid[i][0], grid[i][1], grid[i][2]])
#         if len(row) == 1 and grid[i][0] != 0:
#             fRow = row
#             return grid[i][0]

#     for i in range(len(grid)):
#         col = set([grid[0][i], grid[1][i], grid[2][i]])
#         if len(col) == 1 and grid[0][i] != 0:
#             fCol = col
#             return grid[0][i]

#     diag1 = set([grid[0][0], grid[1][1], grid[2][2]])
#     diag2 = set([grid[0][2], grid[1][1], grid[2][0]])

#     if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
#         return grid[1][1]

#     return 0


def checkDraw(grid):
    Z = 9
    for i in range(len(grid)):
        for y in range(len(grid)):
            if grid[i][y] == 0:
                Z = Z - 1
    return Z


while True:
    
    inputCoor1(grid)
    checkGrid(grid)
    printGrid(grid)
    if elapsed_turns !=9:
        if checkGrid(grid) != 0:
            print(checkGrid(grid), "wins")
            break
        else:
            inputCoor2(grid)
            checkGrid(grid)
            printGrid(grid)
            if checkGrid(grid) != 0:
                print(checkGrid(grid), "wins")
                break
    else:
        print("Draw")
        break