
sizeOfBoard = int(input("Enter x size: "))
# ySizeOfBoard = int(input("Enter y size: "))

def dot_printBoard():
    print(' ---' * sizeOfBoard)

def slash_printBoard():
    print('|   ' * (sizeOfBoard + 1))


def main():
    
    for i in range(sizeOfBoard):
        dot_printBoard()
        slash_printBoard()
    dot_printBoard()


if __name__ == "__main__":
    main()