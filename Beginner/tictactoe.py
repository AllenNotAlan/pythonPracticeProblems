from checkTicTacToe import checkGrid #imported from step 3 of challenge

#grid created
grid = [[0,0,0],
        [0,0,0],
        [0,0,0]]

#no of turns counted
elapsed_turns = 0

#input function for player X
def inputCoor1(grid):
    x, y = input("Player 1 enter two numbers: ").split()
    x, y = [int(x), int(y)]
    if grid[x][y] != 0:
        print("Already occupied")
        inputCoor1(grid)
    else:
        grid[x][y] = "X"
        global elapsed_turns
        elapsed_turns += 1

#input function for player O
def inputCoor2(grid):
    x, y = input("Player 2 enter two numbers: ").split()
    x, y = [int(x), int(y)]
    if grid[x][y] != 0:
        print("Already occupied")
        inputCoor2(grid)
    else:
        grid[x][y] = "O"
        global elapsed_turns
        elapsed_turns += 1

#print grid function
def printGrid(grid):
    for i in range(len(grid)):
        print(grid[i])

#main function
def main():
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

if __name__ == "__main__":
    main()