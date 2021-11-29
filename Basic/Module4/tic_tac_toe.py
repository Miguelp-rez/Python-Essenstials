from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    for i in range(3):
        print("|       |       |       |")
        print("|  ", board[i][0], "  |  ", board[i][1], "  |  ", board[i][2], "  |")
        print("|       |       |       |")
        print("+-------+-------+-------+")
        


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            square = int(input("Enter your move: "))
            if square > 0 and square < 10:
                square -= 1
                row = square // 3
                column = square % 3
                if (row,column) not in free_fields:
                    print("That square is not available")
                else:
                    board[row][column] = "O"
                    break
            else:
                print("Please enter a valid square number")
        except ValueError:
            print("Please, enter an integer value")
        

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ["X", "O"]:
                free_fields.append((i,j))
    return free_fields


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    # Players have to control one of the following lines to win
    winning_lines = [
        (1,2,3),
        (4,5,6),
        (7,8,9),
        (1,4,7),
        (2,4,8),
        (3,6,9),
        (1,5,9),
        (3,5,7)
        ]
    counter = 0 # Number squares controlled per line
    for line in winning_lines:
        for square in line:
            square -= 1
            row = square // 3
            column = square % 3
            if board[row][column] == sign:
                counter += 1
            else:
                break # No need to keep cheking this line
        if counter == 3:
            return True 
        else:
            counter = 0 # Reset counter before cheking a new line
    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    column, row = 1, 1 # Just to enter the loop
    while (row, column) not in free_fields:
        square = randrange(10)
        row = square // 3
        column = square % 3
    board[row][column] = "X"


# The computer always marks the middle of the board in its first move
board = [
    [1, 2, 3],
    [4, "X", 6],
    [7, 8, 9]
    ]

free_fields = make_list_of_free_fields(board)
display_board(board)
while True:
    enter_move(board)
    display_board(board)
    if victory_for(board, "O"):
        print("You won!")
        break
    free_fields = make_list_of_free_fields(board)
    draw_move(board)
    display_board(board)
    if victory_for(board, "X"):
        print("You loose!")
        break
    free_fields = make_list_of_free_fields(board)
    if free_fields == []:
        print("It's a tie!")
        break



    
