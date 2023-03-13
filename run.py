from random import randint


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


class User(Board):
    def __init__(self, board):
        """
        Initialize user class
        """
        super().__init__(board)
        self.create_ships()

    def guess(self):
        """
        Allows user to choose the spot they wish to hit
        """
        while True:
            row = input('Please enter a ship row 1-5 : ').upper()
            while row not in ['1', '2', '3', '4', '5']:
                print("Please enter a valid row ")
                row = input('Please enter a ship row 1-5 : ')

            column = input('Please enter a ship column A-E : ').upper()
            while column not in ['A', 'B', 'C', 'D', 'E']:
                print("Please enter a valid column ")
                column = input('Please enter a ship column A-E : ')

            row, column = int(row)-1, self.let_to_num[column]
            if self.print_board[row][column] != ' ':
                print('You already guessed that!')
                continue
            break
        return row, column


class Computer(Board):
    def __init__(self, board):
        """
        Initialize Computer class
        """
        super().__init__(board)
        self.create_ships()

    def choice(self):
        """
        Allows computer to choose the spot they wish to hit
        """
        ship_r, ship_cl = randint(0, 4), randint(0, 4)
        while self.board_pattern[ship_r][ship_cl] == '-':
            ship_r, ship_cl = randint(0, 4), randint(0, 4)
        return ship_r, ship_cl


def print_boards(u_board, c_board):
    """
    Prints two game boards to the console, one for the user and another for the computer
    """
    print('  A B C D E ', '\t  A B C D E ',)
    print('  _________' '\t  _________',)
    row_num = 1
    for row in range(5):
        print("%d|%s|" % (row_num, "|".join(u_board[row])),
              "\t%d|%s|" % (row_num, "|".join(c_board[row])))
        row_num += 1
    print()


def main():

    print('------------------------------------------------------------------')
    print('--------------| Welcome to the Combat of Battleship |-------------')
    print('------------------------------------------------------------------\n')
    print('Test your luck against the computer in this game of battleship!\n')
    print("Guess the positions of the 5 hidden ships on your opponent's board before the computer beats you to it!\n")
    
    board_pattern = [[' ']*5 for x in range(5)]
    user = User(board_pattern)
    computer = Computer(board_pattern)
    print_boards(u_board=user.toList(), c_board=computer.toList())

    while True:
        row, column = user.guess()
        rowC, columnC = computer.choice()
        print('You selected the coordinates: (%d, %d) \nThe computer chose: (%d, %d)'
              % (row+1, column+1, rowC+1, columnC+1))

        score = user.score(row, column)
        computer.score(rowC, columnC)
        print_boards(u_board=user.toList(), c_board=computer.toList())

        if score:
            print('Congratulations you have hit the battleship!')
        else:
            print('Sorry, you missed!')

        if user.count == 5:
            if user.score_val > computer.score_val:
                print("Congratulations! You have sunk all the battleships, you win!")
            elif user.score_val == computer.score_val:
                print("Oops! It's a draw!")
            else:
                print("You lose!")
            print('Your score is: %d'%user.score_val)
            print("The computer's score is: %d"%computer.score_val)
            break
        print('-'*50)
        print('\n Select again: \n')
        user.count += 1
    print('Game Over!')

if __name__ == "__main__":
    main()