import random

class Game_board:
    def __init__(self, rows, columns, mines):
        self.num_rows = rows
        self.num_columns = columns
        self.num_mines = mines
        self.is_first_turn = True
        self.mine_field = []

        #creates an array of size num_rows x num_columns full of '0's
        for row in range(self.num_rows):
            self.mine_field.append([])
            for column in range(self.num_columns):
                self.mine_field[row].append(0)

    #populate the board with mines excluding tiles touching first choice
    def place_mines(self, x, y):  
        mine_counter = self.num_mines

        #switch values of tiles around first choice from zero to X
        for row in range(x-1, x+2):
            for column in range(y-1, y+2):
                if row in range(0, self.num_rows) and column in range(0, self.num_columns):  
                    self.mine_field[row][column] = 'X'
        
        #add specified number of mines to board in random tiles excluding x'd out tiles
        while mine_counter != 0:
            rand_row = random.randrange(0, self.num_rows)
            rand_col = random.randrange(0, self.num_columns)
            if self.mine_field[rand_row][rand_col] == 0:
                self.mine_field[rand_row][rand_col] = '*'
                mine_counter -= 1

    def fill_board(self):
        for x in range(self.num_rows):
            for y in range(self.num_columns):             
                if self.mine_field[x][y] != '*':          #iterate through each tile that is not a mine
                    mine_count = 0
                    for row in range(x-1, x+2):           #for each tile iterate through all the tiles around it counting mines
                        for column in range(y-1, y+2):
                            if row in range(0, self.num_rows) and column in range(0, self.num_columns):  #if tile is on board
                                if self.mine_field[row][column] == '*':
                                    mine_count += 1
                    self.mine_field[x][y] = mine_count




