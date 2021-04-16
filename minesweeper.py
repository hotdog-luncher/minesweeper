from gameboard import Game_board
from userboard import User_board


#testing

x = Game_board(10, 10, 10)
x.place_mines(4,7)
x.fill_board()

y = User_board(x)

#row, column = y.get_coords()
#print(row, column)
#y.add_mines()
#y.display_board()
#y.explode()

#y.unflag()
#y.unflag()
#y.unflag()
#y.explode()
y.open_tile(2,2)
y.open_zeros(2,2)
y.display_board()
y.place_flag()
y.place_flag()
y.place_flag()
y.double_click()
y.display_board()