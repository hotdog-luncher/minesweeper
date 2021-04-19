class User_board:
    def __init__(self, game_board):
        self.num_rows = game_board.num_rows
        self.num_columns = game_board.num_columns
        self.num_mines = game_board.num_mines
        self.unopened_tiles = self.num_rows * self.num_columns
        self.mine_field = game_board.mine_field
        self.user_array = []
        self.flag_set = set()
        self.mine_set = game_board.mine_set
        self.play_game = 'Y'
        self.game_over = False

        for row in range(self.num_rows):        #creates an array of size num_rows x num_columns full of '-'s
            self.user_array.append([])
            for column in range(self.num_columns):
                self.user_array[row].append('-')

    
    def get_coords(self):                       #get row and column coordinates and validate input, then return them          
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

    def display_board(self):                    #display user board, including row and column numbers, opened tiles, dashes, and flags
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

    def add_mines(self):                        #add mines from the game board to the user board
        for coord in self.mine_set:
            x = coord[0]
            y = coord[1]
            self.user_array[x][y] = '*'

    def explode(self):                          #call add mines, check for bad flags and display the board
        self.add_mines()
        bad_flag = self.flag_set.difference(self.mine_set)
        
        for coord in bad_flag:
            x = coord[0]
            y = coord[1]
            self.user_array[x][y] = 'X'
        
        self.display_board()

        while True:
            self.play_game = input("you lose! would you like to play again? (Y/N)").upper()
            if self.play_game in ['Y', 'N']: 
                break    
        self.game_over = True
            
    def place_flag(self):                       #allows user to place flag representing a mine
        print("Place a flag to mark a suspected mine")
        row, column = self.get_coords() 

        if self.user_array[row][column] == 'F':
            print("This tile is already flagged \n")
            self.display_board()
            return
        
        elif self.user_array[row][column] != '-':
            print("This tile has already been opened \n")
            self.display_board()
            return
        
        else:
            self.user_array[row][column] = 'F'
            self.flag_set.add((row,column))
        
        self.display_board()

    def unflag(self):                           #allows user to remove a previously placed flag
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

    def open_tile(self, x, y):                  #sets user array equal to minefield at a given tile
        self.user_array[x][y] = self.mine_field[x][y]
        self.unopened_tiles -= 1

    def get_unopened_neighbors(self, x, y):     #takes in coords and builds a set of tile coords for tiles that are neighbors, in range and unopened ('-' on userboard) and returns it
        unopened_set = set()

        for row in range(x-1, x+2):                 
            for column in range(y-1, y+2):
                if row in range(0, self.num_rows) and column in range(0, self.num_columns):  
                    if self.user_array[row][column] == '-':
                        unopened_set.add((row,column))
        
        return unopened_set

    def open_zeros(self, x, y):                 #opens each tile that is a zero, a neighbor and not a bomb and repeats action for each adjacent tile
        if self.user_array[x][y] != 0:
            return
        
        else:
            unopened_neighbor_set = self.get_unopened_neighbors(x,y)
            while unopened_neighbor_set:
                coords = unopened_neighbor_set.pop()
                self.open_tile(coords[0],coords[1])
                if self.mine_field[coords[0]][coords[1]] == 0:
                    unopened_neighbor_set = unopened_neighbor_set.union(self.get_unopened_neighbors(coords[0],coords[1]))

    def double_click(self):                     #gets coords, if tile is open, and tile value == the number of neighbor tiles with mines open all neighbor tiles and call open zeros on them 
        x, y = self.get_coords()
        tile_value = self.user_array[x][y]
        flag_count = 0

        if tile_value == '-':
            print('Tile is not yet opened\n')
            return
        
        for row in range(x-1, x+2):                    #for each tile iterate through all the tiles around it counting flags
             for column in range(y-1, y+2):
                if row in range(0, self.num_rows) and column in range(0, self.num_columns):  #if tile is on board
                    if self.user_array[row][column] == 'F':
                        flag_count += 1
        
        if flag_count > tile_value:
            print("too many flags around tile\n")

        elif tile_value > flag_count:
            print("not enough flags around tile\n") 

        else:
            for row in range(x-1, x+2):                  #for each tile iterate through all the tiles around it 
             for column in range(y-1, y+2):
                if row in range(0, self.num_rows) and column in range(0, self.num_columns):  #if tile is on board
                    if self.user_array[row][column] == '-':                                  #open tile, if bomb explode
                        if self.mine_field[row][column] == '*':
                            self.explode()
                        self.open_tile(row, column)
                        self.open_zeros(row, column)
            self.display_board()

    def choose(self, x, y):                     #takes in coords, if bomb explode, if '-' open tile and call open zeros
        if self.user_array[x][y] == 'F':
            print("This tile is flagged as a mine and cannot be selected\n")
            self.display_board()
            return
        
        if self.user_array[x][y] != '-':
            print("This tile has already been opened\n")
            self.display_board()
            return
        
        if self.mine_field[x][y] == '*':
            self.explode()
            return

        self.open_tile(x, y)
        self.open_zeros(x,y)
        self.display_board()

        if self.unopened_tiles == self.num_mines:
            while True:
                self.play_game = input("you win! would you like to play again? (Y/N)").upper()
                if self.play_game in ['Y', 'N']: 
                    break 
            self.game_over = True


        

        
        

        


