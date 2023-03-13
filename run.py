from random import randint

board_pattern = [[' ']*5 for x in range(5)]
let_to_num={'A':0,'B':1, 'C':2,'D':3,'E':4}

def print_boards(board):
    """
    Prints two game boards to the console, one for the user and another for the computer
    """
    print('  A B C D E ', '\t  A B C D E ',)
    print('  _________' '\t  _________',)
    row_num=1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)),"\t%d|%s|" % (row_num, "|".join(row)))
        row_num += 1
    print()

def create_ships():
    """
    Randomly generates 5 ships and places them on the board
    """
    for ship in range(5):
        ship_r, ship_cl = randint(0,4), randint(0,4)
        while board_pattern[ship_r][ship_cl] =='X':
            ship_r, ship_cl = randint(0, 4), randint(0, 4) 
        board_pattern[ship_r][ship_cl] = 'X'

def user_guess():
    """
    Allows used to choose the spot they wish to hit
    """
    while True:
        #Enter the row number between 1 to 5
        row = input('Please enter a ship row 1-5 : ').upper()
        while row not in ['1','2','3','4','5']:
            print("Please enter a valid row ")
            row = input('Please enter a ship row 1-5 ')
        #Enter the Ship column from A TO E
        column = input('Please enter a ship column A-E ').upper()
        while column not in ['A','B','C','D','E']:
            print("Please enter a valid column ")
            column = input('Please enter a ship column A-E ')
        row, column = int(row)-1, let_to_num[column]
        if board_pattern[row][column] == '-':
            print('You already guessed that')
            continue
        break
    return row, column

def count_hits():
    count = 0
    for row in Guess_Pattern:
        for column in row:
            if column == 'X':
                count += 1
    return count

def main():
    computer_score, user_score = 0, 0
    # board_pattern = [[' ']*5 for x in range(5)]
    # let_to_num={'A':0,'B':1, 'C':2,'D':3,'E':4}

    print('------------------------------------------------------------------')
    print('--------------| Welcome to the Combat of Battleship |-------------')
    print('------------------------------------------------------------------\n')
    print('Test your luck against the computer in this game of battleship!\n')
    print("Guess the positions of the 5 hidden ships on your opponent's board before the computer beats you to it!\n")
    print_boards(board_pattern)
    create_ships()
    row, column = user_guess()

main()