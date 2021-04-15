from gameboard import Game_board
from userboard import User_board


#testing

x = Game_board(4,4, 3)
x.place_mines(4,7)
#print(x.mine_field)

#x.fill_board()
#print(x.mine_field)

y = User_board(x)

#row, column = y.get_coords()
#print(row, column)
#y.add_mines()
y.display_board()
#y.explode()
#y.place_flag()
#y.place_flag()
#y.place_flag()
#y.unflag()
#y.unflag()
y.unflag()
#y.explode()
y.display_board()