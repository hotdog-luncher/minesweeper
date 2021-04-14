from gameboard import Game_board
from userboard import User_board


#testing

x = Game_board(15, 15 ,7)
#x.place_mines(0,1)
#print(x.mine_field)

#x.fill_board()
#print(x.mine_field)

y = User_board(x)

#row, column = y.get_coords()
#print(row, column)

y.display_board()