def print_boards(board):
    print('  A B C D E ', '\t  A B C D E ',)
    print('  _________' '\t  _________',)
    row_num=1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)),"\t%d|%s|" % (row_num, "|".join(row)))
        row_num += 1
    print()

def create_ships():
    pass

def get_ship_location():
    pass

def count_hits():
    pass

def main():
    computer_score, user_score = 0, 0
    board_pattern=[[' ']*5 for x in range(5)]
    let_to_num={'A':0,'B':1, 'C':2,'D':3,'E':4}

    print('------------------------------------------------------------------')
    print('--------------| Welcome to the Combat of Battleship |-------------')
    print('------------------------------------------------------------------\n')
    print('Test your luck against the computer in this game of battleship!\n')
    print("Guess the positions of the 5 hidden ships on your opponent's board before the computer beats you to it!\n")
    print_boards(board_pattern)

main()