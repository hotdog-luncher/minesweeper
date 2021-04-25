from gameboard import Game_board
from userboard import User_board
import time
import os

def create_gameboard():
    rows = 0
    columns = 0
    mines = 0

    while True: 
        choice = input("Please select a game:\nB (beginner) I (Intermediate), E (Expert), C (Custom):").upper()
        print()
        if choice in ['B', 'I', 'E', 'C']:
            break
    
    if choice == 'B':
        rows = 9
        columns = 9
        mines = 10

    if choice == 'I':
        rows = 16
        columns = 16
        mines = 40

    if choice == 'E':
        rows = 16
        columns = 30
        mines = 99
       
    if choice == 'C':
        print('lets create a custom board!\n') 
        while True:                                                                              #get row
            while True:
                try:
                    rows = int(input('enter the number of rows from 1 to {0}: '.format(max_rows)))      #make sure entry is a number
                    break
                except ValueError:
                    print("thats not a number! \n")

            if rows not in list((range(1, max_rows+1))):                                         #make sure entry is in range              
                print("Please enter a number from 1 to {0}\n".format(max_rows))
            else:
                break
        
        while True:                                                                              #get column
            while True:
                try:
                    columns = int(input('enter the number of columns from 8 to {0}: '.format(max_columns)))  #make sure entry is a number
                    break
                except ValueError:
                    print("thats not a number! \n")

            if columns not in list((range(8, max_columns+1))):                                    #make sure entry is in range              
                print("Please enter a number from 8 to {0}\n".format(max_columns))
            else:
                break
        
        while True:                                                                              #get mines
            while True:
                try:
                    mines = int(input('enter the number of mines from 1 to {0}: '.format((columns * rows)-1)))  #make sure entry is a number
                    break
                except ValueError:
                    print("thats not a number! \n")

            if mines not in list((range(1, (columns * rows)-1))):                        #make sure entry is in range              
                print("Please enter a number from 1 to {0}\n".format(columns * rows -1))
            else:
                break
        
    return Game_board(rows, columns, mines)
    
play_game = 'Y'
max_rows = 70
max_columns = 88 

while play_game == 'Y':                                      #master game loop
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Minesweeper\n")

    game_board = create_gameboard()
    user_board = User_board(game_board)
    
    while user_board.game_over == False:                      #inner game loop
        while True:
            user_board.display_board()
            rem_mines = user_board.num_mines - len(user_board.flag_set)
            print('\n{0} seconds have elapsed'.format(int(time.monotonic())-user_board.game_start_time))
            print('{0} mines remaining \n'.format(rem_mines))
            choice = input("What would you like to do?\nC (choose), F (flag), U (unflag), D (double click) Q (quit)").upper()
            if choice in ['C', 'F', 'U', 'D', 'Q']:
                break   
    
        if choice == 'C':
            x, y = user_board.get_coords()
            if game_board.is_first_turn == True:               #fill gameboard after initial choice insuring a first choice of a 0 tile
                game_board.place_mines(x,y)
                game_board.fill_board()
                user_board.update_minefield(game_board)
                               
            user_board.choose(x,y)

        if choice == 'F':
            user_board.place_flag()
    
        if choice == 'U':
            user_board.unflag()
    
        if choice == 'D':
            user_board.double_click()

        if choice == 'Q':
            user_board.play_game = 'N'

        play_game = user_board.play_game

        if user_board.play_game == 'N':
            break
