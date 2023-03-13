from random import randint

board_pattern = [[' ']*5 for x in range(5)]
let_to_num={'A':0,'B':1, 'C':2,'D':3,'E':4}
computer_score, user_score = 0, 0

class Board:
    def __init__(self, board):
        """
        Initializing boards
        """
        self.board_pattern = board
        self.print_board = [[' ']*5 for x in range(5)]
        self.let_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
        self.score_val = 0
        self.count = 1

    def create_ships(self):
        """
        Randomly generates 5 ships and places them on the board
        """
        for ship in range(5):
            ship_r, ship_cl = randint(0, 4), randint(0, 4)
            while self.board_pattern[ship_r][ship_cl] == 'X':
                ship_r, ship_cl = randint(0, 4), randint(0, 4)
            self.board_pattern[ship_r][ship_cl] = 'X'

    def score(self,row,col):
        """
        manipulate scores and marks the hit spot
        """
        temp = self.score_val
        if self.board_pattern[row][col] == 'X':
            self.print_board[row][col] = 'X'
            self.score_val +=1
            
        else:
            self.board_pattern[row][col] = '-'
            self.print_board[row][col] = '-'

        return self.score_val>temp

    def toList(self):
        """
        return the board for printing
        """
        return self.print_board

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

# def create_ships():
#     """
#     Randomly generates 5 ships and places them on the board
#     """
#     for ship in range(5):
#         ship_r, ship_cl = randint(0,4), randint(0,4)
#         while board_pattern[ship_r][ship_cl] =='X':
#             ship_r, ship_cl = randint(0, 4), randint(0, 4) 
#         board_pattern[ship_r][ship_cl] = 'X'

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

def computer_choice():
    ship_r, ship_cl = randint(0,4), randint(0,4)
    while board_pattern[ship_r][ship_cl] =='-':
        ship_r, ship_cl = randint(0, 4), randint(0, 4) 
    return ship_r, ship_cl

def count_hits():
    count = 0
    for row in board_pattern:
        for column in row:
            if column == 'X':
                count += 1
    return count

def main():
    # computer_score, user_score = 0, 0
    # board_pattern = [[' ']*5 for x in range(5)]
    # let_to_num={'A':0,'B':1, 'C':2,'D':3,'E':4}

    print('------------------------------------------------------------------')
    print('--------------| Welcome to the Combat of Battleship |-------------')
    print('------------------------------------------------------------------\n')
    print('Test your luck against the computer in this game of battleship!\n')
    print("Guess the positions of the 5 hidden ships on your opponent's board before the computer beats you to it!\n")
    # print_boards(board_pattern)
    # create_ships()
    # row, column = user_guess()
    while True:
        print_boards(board_pattern)
        row,column = user_guess()
        rowC, columnC = computer_choice()
        print('you choice is : (%d, %d) \ncomputer choice is :(%d, %d)' 
            % (row, column+1, rowC+1, columnC+1))
        
        if board_pattern[rowC][columnC] == 'X':
            computer_score +=1
        else:
            board_pattern[rowC][columnC] = '-'
        if board_pattern[row][column] == 'X':
            print('Congratulations you have hit the battleship!')
            board_pattern[row][column] = 'X'
            user_score +=1
        else:
            print('Sorry, you missed!')
            board_pattern[row][column] = '-'
        if  count_hits() == 5:
            if user_score > computer_score:
                print("Congratulations! You have sunk all the battleships, you win!")
            elif user_score == computer_score:
                print("Oops! It's a draw!")
            else:
                print("You lose!")
            print('your score is : %d'%user_score)
            print('the computer score is : %d'%computer_score)
            break
        print('-'*50)
        print('\n Select again: \n')
    if user_score > computer_score:
        print
    print('Game Over!') 

main()