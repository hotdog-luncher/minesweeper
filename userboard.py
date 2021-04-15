class User_board:
    def __init__(self, game_board):
        self.num_rows = game_board.num_rows
        self.num_columns = game_board.num_columns
        self.unopened_tiles = self.num_rows * self.num_columns
        self.mine_field = game_board.mine_field
        self.user_array = []
        self.flag_set = set()
        self.mine_set = game_board.mine_set
        self.play_game = 'y'

        for row in range(self.num_rows):        #creates an array of size num_rows x num_columns full of '-'s
            self.user_array.append([])
            for column in range(self.num_columns):
                self.user_array[row].append('-')

    def get_coords(self):                          #get row and column coordinates and validate input, then return them          
        while True:                                                                    #get row
            while True:
                try:
                    row = int(input("Please enter a row: "))                           #make sure entry is a number
                    break
                except ValueError:
                    print("thats not a number! \n")

            if row not in list((range(1, self.num_rows+1))):                           #make sure entry is on the board
                print("Please enter a number from 1 to {0}\n".format(self.num_rows))
            else:
                break

        while True:                                                                     #get column
            while True:
                try:                                                                    #make sure entry is a number
                    column =  int(input("Please enter a column: "))
                    break
                except ValueError:
                    print("thats not a number! \n")

            if column not in list((range(1, self.num_columns+1))):                      #make sure entry is on the board
                print("Please enter a number from 1 to {0}\n".format(self.num_columns))
            else:
                break

        return row - 1, column - 1

    def display_board(self):                       #display user board, including row and column numbers, opened tiles, dashes, and flags
        x = 1
        print('  ', end= ' ')
        for num in range(1, self.num_columns+1):          
            print(num, end= ' ')
            if num < 10:                           #handle spacing in grid layout when the number goes from single to double digit
                print(' ', end= '')
        for row in range(self.num_rows):
            print()
            print(x, end= ' ')
            if x < 10:
                print(' ', end= '')
            x += 1
            for column in range(self.num_columns):
                print(self.user_array[row][column], end='  ')
        print()

    def add_mines(self):                           #add mines from the game board to the user board
        for coord in self.mine_set:
            x = coord[0]
            y = coord[1]
            self.user_array[x][y] = '*'

    def explode(self):                             #call add mines, check for bad flags and display the board
        self.add_mines()
        bad_flag = self.flag_set.difference(self.mine_set)
        
        for coord in bad_flag:
            x = coord[0]
            y = coord[1]
            self.user_array[x][y] = 'X'
        
        self.display_board()

        new_game = ''
        while new_game not in ['y', 'n']:
            new_game = input("you lose! would you like to play again? (y/n)").lower()     
        
        self.play_game = new_game
            
    def place_flag(self):                          #allows user to place flag representing a mine
        print("Place a flag to mark a suspected mine")
        row, column = self.get_coords() 

        if self.user_array[row][column] == 'F':
            print("This tile is already flagged \n")
            return
        
        elif self.user_array[row][column] != '-':
            print("This tile has already been opened \n")
            return
        
        else:
            self.user_array[row][column] = 'F'
            self.flag_set.add((row,column))
        
        self.display_board()

    def unflag(self):                              #allows user to remove a previously placed flag
        if self.flag_set:
            print("Remove a flag from the board")
            row, column = self.get_coords()
            if self.user_array[row][column] != 'F':
                print("Tile is not flagged")
            else:
                self.user_array[row][column] = '-'
                self.flag_set.remove((row, column))
        else:
            print("There are currently no flags\n")
        self.display_board()
        



