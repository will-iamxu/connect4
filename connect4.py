import turtle 

a = turtle.Turtle()

#Displays the game board.
def display():
    ###Part 1### - making background color grey
    turtle.Screen().bgcolor("black")
    a.hideturtle()
    a.speed(9999)
    
    for i in range(-360, 480, 120):
        for j in range(-460, 245, 117):
            circle(i,j)

def circle(x,y, color = "white"):
    a.penup()           # moves the circle
    a.goto(x, y) 
    
    a.pendown()          #Draws the circle
    a.begin_fill()
    a.circle(51.25)    
    a.color(color)
    a.end_fill()

filex = open("moves_made.txt","w")
filex.write("Recorded moves from game: (column, row)\n")


grid = []
player = []

num_rows = 6
num_cols = 7
#Dictionary that will be used to detect if it is a valid move
#Will be updated each move // Key = column , value = height of empty spots (NEED IF STATEMENT TO DETECT ROW < 6)
valid_moves = {1 : 0 , 2 : 0 , 3 : 0 , 4 : 0 , 5 : 0 , 6 : 0 , 7 : 0}

def make_grid():
  '''Makes the grid'''
  #makes the grid of the array
  for i in range(num_rows):
    columns = []
    for j in range(num_cols):
        columns.append(-1)
    grid.append(columns)
def is_column_full(index):
  '''checks if the column being placed is full'''
  #if grid is not full continue game
  try:
    if(grid[valid_moves[index + 1]][index] == -1 and valid_moves[index + 1] < 6):
      return False
    else:
      return True
  except:
    return True

def place_chip(index, chipNum): #0 player 1 // 1 player 2
  '''places the chip'''
  if(index < 0 or index > num_cols or is_column_full(index)):
      return False
  #i = rows
  i = num_rows - 1
  while i > -1:
      if(grid[valid_moves[index+1]][index] == -1):
          grid[valid_moves[index+1]][index] = chipNum 
          valid_moves[index+1] += 1
          return True
      i -= 1
      return False
def is_full():
  #checks if the whole grid is full
    for i in range(num_rows):
      if(not is_column_full(i)):
        return False
    return True

def get_winner():
    #Boolean variable to detect if there is a win
    win = False
    
    
  #checks rows
    for i in range(num_rows):
        for j in range(num_cols-3):
            if((grid[i][j] == grid[i][j + 1]) and (grid[i][j] != -1)):
                if(grid[i][j + 1] == grid[i][j + 2]):
                    if(grid[i][j + 2] == grid[i][j + 3]):
                        win = True
                        return get_chip(i,j)
    #checks diagonal
    for i in range(num_rows-3):
        for j in range(num_cols):
            if((grid[i][j] == grid[i+1][j]) and (grid[i][j] != -1)):
                if(grid[i+1][j] == grid[i+2][j + 2]):
                    if(grid[i+2][j] == grid[i+3][j]):
                        win = True
                        return get_chip(i,j)
    #checks diagonal
    for i in range(num_rows-3):
        for j in range(num_cols-3):
            if((grid[i][j] == grid[i+1][j+1]) and (grid[i][j] != -1)):
                if(grid[i+1][j+1] == grid[i+2][j+2]):
                    if(grid[i+2][j+2] == grid[i+3][j+3]):
                        win = True
                        return get_chip(i,j)
                    
    #checks backward diagonal
    for i in range(num_rows-3):
        for j in range(3,num_cols):
            if((grid[i][j] == grid[i+1][j-1]) and (grid[i][j] != -1)):
                if(grid[i+1][j-1] == grid[i+2][j-2]):
                    if(grid[i+2][j-2] == grid[i+3][j-3]):
                        win = True
                        return get_chip(i,j)
                    
    #Checks columns 
    for j in range(num_cols):
        for i in range(num_rows-3):
            if((grid[i][j] == grid[i+1][j]) and (grid[i][j] != -1)):
                if(grid[i+1][j] == grid[i+2][j]):
                    if(grid[i+2][j] == grid[i+3][j]):
                        win = True
                        return get_chip(i,j)
            
                    
    if win == False:
        return -1

def get_chip(row, col):
  #gets the chips
    return grid[row][col]

def get_names():
  #gets the names of the players
    player.append(input('Enter player 1\'s name: '))
    player.append(input('Enter player 2\'s name: '))

def play():
  options()
  make_grid()
  get_names()
  #Displays initial game board
  display()
  while(get_winner() == -1):
      if(is_full() == True):
          print("Both players are stupid and dumb and managed to lose together. Congratulations though.")
          break
      #Player 1 move
      position1 = int(input(f"Which column would you like to place your chip {player[0]}? "))
      writemoves(position1)
      while(place_chip((position1 - 1), 0) == False):
          position1 = int(input(f"Column is full. Which column would you like to place your chip {player[0]}? "))    
      #Displays the game board using player 1's move
      circle((-360 + 120*(position1-1)), (-460 + 117*(valid_moves[position1])),"blue")
      
      if(get_winner() != -1):
          break
      #Player 2 move
      position2 = int(input(f"Which column would you like to place your chip {player[1]}? "))
      writemoves(position2)
      while(place_chip((position2 - 1), 1) == False):
          position2 = int(input(f"Column is full. Which column would you like to place your chip {player[1]}? "))    
      #Displays the game board using player 2's move 
      circle((-360 + 120*(position2-1)), (-460 + 117*(valid_moves[position2])),"yellow")
      
      if(get_winner() != -1):
          break
  print(f"Congratulations {player[get_winner()]} you win!!\U0001F600\U0001F600\U0001F600")

def writemoves(position):
    filex.write(f"{position},{(valid_moves[position]+1)}\n")
    
def options():
  while True:
    op = input("Would you like to view the instructions before playing? ")
    try:
      if op == "yes":
         print("OBJECTIVE:To be the first player to connect 4 of the same colored discs in a row (either vertically, horizontally, or diagonally)")
         print("HOW TO PLAY: First, decide who goes first and what color each player will have. Players must alternate turns, and only one disc can be dropped in each turn. On your turn, drop one of your colored discs from the top into any of the seven slots. The game ends when there is a 4-in-a-row or a stalemate. The starter of the previous game goes second on the next game.")
         break
      elif op == "no":
          break
    except:
      op = input("Bad input U+274C")

play()

filex.close()