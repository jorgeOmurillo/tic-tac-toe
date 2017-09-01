def check_grid(n):
    found = False

    for i in range(len(n)):
        if n[i] == ' ':
            found = True

    return found

def print_grid(grid):
    print(" " + str(grid[0]) + " | " + str(grid[1]) + " | " + str(grid[2]) + "          " + " 1 " + " | " + " 2 "  + " | " + " 3 ")
    print("-----------         ---------------")
    print(" " + str(grid[3]) + " | " + str(grid[4]) + " | " + str(grid[5]) + "          " + " 4 " + " | " + " 5 "  + " | " + " 6 ")
    print("-----------         ---------------")
    print(" " + str(grid[6]) + " | " + str(grid[7]) + " | " + str(grid[8]) + "          " + " 7 " + " | " + " 8 "  + " | " + " 9 ")

def win_or_lose(grid):
    if (grid[0] == 'X' and grid[1] == 'X' and grid[2]) == 'X' or    \
            (grid[3] == 'X' and grid[4] == 'X' and grid[5]) == 'X' or   \
            (grid[6] == 'X' and grid[7] == 'X' and grid[8]) == 'X' or   \
            (grid[0] == 'X' and grid[3] == 'X' and grid[6]) == 'X' or   \
            (grid[1] == 'X' and grid[4] == 'X' and grid[7]) == 'X' or   \
            (grid[2] == 'X' and grid[5] == 'X' and grid[8]) == 'X' or   \
            (grid[0] == 'X' and grid[4] == 'X' and grid[8]) == 'X' or   \
            (grid[2] == 'X' and grid[4] == 'X' and grid[6]) == 'X':
        print("Player 1 wins!")
        return True

    if (grid[0] == 'O' and grid[1] == 'O' and grid[2]) == 'O' or   \
            (grid[3] == 'O' and grid[4] == 'O' and grid[5]) == 'O' or  \
            (grid[6] == 'O' and grid[7] == 'O' and grid[8]) == 'O' or  \
            (grid[0] == 'O' and grid[3] == 'O' and grid[6]) == 'O' or  \
            (grid[1] == 'O' and grid[4] == 'O' and grid[7]) == 'O' or  \
            (grid[2] == 'O' and grid[5] == 'O' and grid[8]) == 'O' or  \
            (grid[0] == 'O' and grid[4] == 'O' and grid[8]) == 'O' or  \
            (grid[2] == 'O' and grid[4] == 'O' and grid[6]) == 'O':
        print("Player 2 wins!")
        return True

def main(grid):
    while True:
        p1 = 0
        p2 = 0

        ## Player 1 selection
        while check_grid(grid):
            p1 = input("Input your option player 1.\n")
            try:
                if int(p1) in range(1,10):
                    p1 = int(p1)

                    if grid[p1-1] is not " ":
                        print_grid(grid)
                        print("This value is taken, please choose a different option.\n")
                    else:
                        break
                else:
                    print_grid(grid)
                    print("This value is incorrect. Try again.\n")
                    pass

            except ValueError:
                print_grid(grid)
                print("This is not a valid number.\n")
 
        if check_grid(grid):
            grid[p1-1] = 'X'
        else:
            print("Game is a draw.\n")
            break

        print_grid(grid)

        if win_or_lose(grid):
            break
        
        ## Player 2 selection
        while check_grid(grid):
            p2 = input("Input your option player 2.\n")
            try:
                if int(p2) in range(1,10):
                    p2 = int(p2)

                    if grid[p2-1] is not " ":
                        print_grid(grid)
                        print("This value is taken, please choose a different option.\n")
                    else:
                        break
                else:
                    print_grid(grid)
                    print("This is not a valid number.\n")
                    pass
            except ValueError:
                print_grid(grid)
                print("This is not a valid number.\n")

        if check_grid(grid):
            grid[p2-1] = 'O'
        else:
            print("Game is a draw.\n")

        print_grid(grid)

        if win_or_lose(grid):
            break

if __name__ == "__main__": 
    grid = [' ']*9
    print_grid(grid)

    main(grid)
