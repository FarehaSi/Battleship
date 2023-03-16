from random import randint


class Board:
    def __init__(self, board):
        """
        Initializing boards
        """
        self.board_pattern = board
        self.print_board = [[' ']*5 for x in range(5)]
        self.score_val = 0
        self.count = 0
        self.create_ships()

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
        Manipulate scores and marks the hit spot
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
        Return the board for printing
        """
        return self.print_board

    def count_hits(self):
        count = 0
        for row in self.print_board:
            for column in row:
                if column == 'X':
                    count += 1
        self.count = count

    def find_cell(self,cell):
        """
        Convert the number to coordinates
        """
        cel = {}
        cell = int(cell) - 1
        for i in range(5):
            for j in range(5):
                cel[j+i*5] = [i,j]
        return cel[cell][0],cel[cell][1]

    def get_num(self,row,col):
        """
        Convert the coordinates to a number between 1 to 25
        """
        return (row*5)+col + 1


class User(Board):
    def __init__(self, board):
        """
        Initialize user class
        """
        super().__init__(board)

    def guess(self):
        """
        Allows user to choose the spot they wish to hit
        """
        while True:
            cell = input('Please enter a cell number between 1 to 25:\n').upper()
            while cell not in [str(i) for i in range(1,26)]:
                print("Please enter a valid cell ")
                cell = input('Please enter a cell no 1-25 :\n')

            row, column = self.find_cell(cell)
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

    def choice(self):
        """
        Allows computer to choose the spot they wish to hit
        """
        ship_r, ship_cl = randint(0, 4), randint(0, 4)
        while self.print_board[ship_r][ship_cl] != ' ':
            ship_r, ship_cl = randint(0, 4), randint(0, 4)
        return ship_r, ship_cl


def print_boards(u_board, c_board):
    """
    Prints two game boards to the console, one for the user and another for the computer
    """
    print('    Player ', '\t  Computer ','\t    Reference \n')
    row_num = 1
    for row in range(5):
        ref = []
        for i in range(1,6):
            val  = str(i + (row_num-1)*5)
            if len(val) == 1 :
                ref.append(val+" ")
            else:
                ref.append(val)

        print("%d|%s|" % (row_num, "|".join(u_board[row])),
            "\t%d|%s|" % (row_num, "|".join(c_board[row])),
            "\t%d|%s|" % (row_num, "|".join(ref)))
        row_num += 1
    print()


def main():

    print('------------------------------------------------------------------')
    print('--------------| Welcome to the Combat of Battleship |-------------')
    print('------------------------------------------------------------------\n')
    print('Test your luck against the computer in this game of battleship!\n')
    print("Guess the positions of the 5 hidden ships on your opponent's board before the   computer beats you to it!\n")
    
    user = User([[' ']*5 for x in range(5)])
    computer = Computer([[' ']*5 for x in range(5)])
    print_boards(u_board=user.toList(), c_board=computer.toList())

    while True:
        row, column = user.guess()
        rowC, columnC = computer.choice()
        print('\nYou selected: %d \nThe computer chose: %d \n'
            % (user.get_num(row, column), computer.get_num(rowC, columnC)))
        score_user = user.score(row, column)
        score_computer = computer.score(rowC, columnC)
        print_boards(u_board=user.toList(), c_board=computer.toList())
        user.count_hits()
        computer.count_hits()

        if score_user:
            print('Congratulations you have hit the battleship!')
        else:
            print('You missed!')

        if score_computer:
            print('The computer has hit the battleship!\n')
        else:
            print('The computer missed!\n')

        if user.count == 5 or computer.count == 5:
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
        print('\nTake your next turn! \n')

    print('Game Over!')

if __name__ == "__main__":
    main()