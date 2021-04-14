class User_board:
    def __init__(self, game_board):
        self.num_rows = game_board.num_rows
        self.num_columns = game_board.num_columns
        self.unopened_tiles = self.num_rows * self.num_columns
        self.mine_field = game_board.mine_field
        self.user_array = []
        self.flag_set = set()
        self.mine_set = game_board.mine_set

        for row in range(self.num_rows):        #creates an array of size num_rows x num_columns full of '-'s
            self.user_array.append([])
            for column in range(self.num_columns):
                self.user_array[row].append('-')

    def get_coords(self):                          #get row and column coordinates and validate input          
        while True:                                                                    #get row
            while True:
                try:
                    row = int(input("Please enter a row: "))                           #make sure entry is a number
                    break
                except ValueError:
                    print("thats not a number!")

            if row not in list((range(1, self.num_rows+1))):                           #make sure entry is on the board
                print("Please enter a number from 1 to {0}".format(self.num_rows))
            else:
                break

        while True:                                                                     #get column
            while True:
                try:                                                                    #make sure entry is a number
                    column =  int(input("Please enter a column: "))
                    break
                except ValueError:
                    print("thats not a number!")

            if column not in list((range(1, self.num_columns+1))):                      #make sure entry is on the board
                print("Please enter a number from 1 to {0}".format(self.num_columns))
            else:
                break

        return row , column

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
        for row in range(self.num_rows):
            for column in range(self.num_columns):
                if self.mine_field[row][column] == '*':
                    self.user_array[row][column] = '*'

    def explode(self):
        self.add_mines()
