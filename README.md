# minesweeper

    This is a text based minesweeper program that I built for a Codecademy project.  The course instructions
    didn't give much specific direction, and so using the skills that I had to this point, I tried to 
    replicate the functionality of the original.  

  
  prompts user to enter B (beginner), I (intermediate), E (expert), C (custom):
  
    B: create game board 9x9 with 10 mines
    I: create game board 16x16 with 40 mines
    E: create game board 16x30 with 99 mines
    C: prompt user to enter number of rows, columns and mines
      
  the game displays the blank board, showing the numbers of the rows and columns, and each tile as unopened.  The game handles spacing if the numbers are double digit
    
  user can then select C (choose), F (flag), U (unflag), D (double click) or Q (quit):
  
    C: allows user to select a tile to open
    F: place a flag over a suspected mine
    U: remove a flag
    D: double click an opened tile if the number displayed equals the number of flagged tiles touching it
    Q: exit the game
    
 After each subsequent action, the userboard is updated and displayed along with mines remaining and a timer showing game time elapsed.
 This will continue until the user either opens each tile that is not a mine or selects a mine. 
 
 
 
 
 
 some notes:
 
the game will not allow a mine to be selected on the first turn.  Therefore, the master "gameboard" that is referenced by the program but hidden from the user is
not created until after the first selection
  
when adding mines to the gameboard, the program first reserves all of the tiles around the first choice, insuring that first choice will be a zero if possible.  However, if the number of mines approaches the size of the board, the method will randomly add mines to the appropriate amount of reserved tiles
  
The master gameboard is then generated, including the appropriate number of mines and the corresponding numbers in each of the other tiles
  
choosing a zero tile will cause the game to choose each tile around that tile that is also a zero, opening up a larger section of the board
  
  
  
