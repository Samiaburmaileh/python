# Sami Abu Rmaileh & Malak Raddad 
# ID : 1192325 & ID : 1192408
# We certify that this submission is the original work of members of the group and meets
# the Faculty's Expectations of Originality# Expectations of Originality
# we start the project in 12/5/2023 friday 
import time
import winsound
sound_file1 = "sounds\Welcome.wav"
sound_file2 = "sounds\easy.wav"
sound_file3 = "sounds\Rules.wav"
sound_file4 = "sounds\gameruls.wav"
sound_file5 = "sounds\Enter.wav"
sound_file6 = "sounds\pa1.wav"
sound_file7 = "sounds\pa2.wav"
sound_file8 = "sounds\Restart.wav"
sound_file9 = "sounds\Tie.wav"


# this function for create the board to play 
def CreBoard():
    board = []
    for _ in range(8):
        row = ['_'] * 8
        board.append(row)
    return board

# print the empty board for the user 
def PriBoard(board):
    print("    A B C D E F G H     ")
    for i in range(8, 0, -1):
        row_str = f"{i} │ "
        for j in range(8):
            row_str += board[i-1][j] + " "
        row_str += "│"
        print(row_str)
    print("    A B C D E F G H     ")

# this function is to update the board every turn, he got the board and the postion the user inter and the symbol for the current player
# the first thing he do is to cheak if position is valid then cheak if the postion occupied, then he will cheak if the position is next 
# to a brick or the side walls or next to another brick or at the edges.
def updBoard(board, position, symbol):
    column = ord(position[0].upper()) - ord('A')
    row = int(position[1]) - 1

    # valid position or not
    if not validPos(position):
        print("Invalid position. Try again.")
        return False

    # occupied or not 
    if board[row][column] != '_':
        print("Position already occupied. Try again.")
        return False

    # stacked directly to bordler or not 
    adjacent_positions = [(row, column-1), (row, column+1)]
    valid_positions = adjacent_positions

    if row > 0:
        valid_positions.append((row-1, column))
    if row < 7:
        valid_positions.append((row+1, column))
    if row > 0 and column > 0:
        valid_positions.append((row-1, column-1))
    if row > 0 and column < 7:
        valid_positions.append((row-1, column+1))
    if row < 7 and column > 0:
        valid_positions.append((row+1, column-1))
    if row < 7 and column < 7:
        valid_positions.append((row+1, column+1))

    for adj_row, adj_col in valid_positions:
        if adj_col == -1 or adj_col == 8 or board[adj_row][adj_col] != '_':
            break
    else:
        print("Invalid position. Brick must be stacked directly on the left or right wall, or adjacent/diagonal to another brick, or up and down.")
        return False

    # Update board
    board[row][column] = symbol
    return True

# is full
def BoardFull(board):
    for row in board:
        if '_' in row:
            return False
    return True

# Valied Number 
def validPos(position):
    if len(position) != 2:
        return False
    column = position[0].upper()
    row = position[1]
    return column in 'ABCDEFGH' and row in '12345678'


# check the winner he should be 5 blocks next to each other,in rows, colums and diagonals
def win(board, player_symbol):
    rows = len(board)
    cols = len(board[0])
    
    for row in range(rows):
        for col in range(cols):
            symbol = board[row][col]
            if symbol == player_symbol:
                # Check horizontal win
                if col <= cols - 5:
                    if all(board[row][col+i] == symbol for i in range(5)):
                        if col == 0 or col + 4 == cols - 1:
                            return True

                # Check vertical win
                if row <= rows - 5:
                    if all(board[row+i][col] == symbol for i in range(5)):
                        if row == 0 or row + 4 == rows - 1:
                            return True

                # Check diagonal wins
                if col <= cols - 5 and row <= rows - 5:
                    if all(board[row+i][col+i] == symbol for i in range(5)):
                        if (col == 0 and row == 0) or (col + 4 == cols - 1 and row + 4 == rows - 1):
                            return True

                if col <= cols - 5 and row >= 4:
                    if all(board[row-i][col+i] == symbol for i in range(5)):
                        if (col == 0 and row == rows - 1) or (col + 4 == cols - 1 and row - 4 == 0):
                            return True

    return False

# Function to restart the game
def restart_game():
    print("Restarting the game...")
    print()

# Main game loop
print("Welcome to the Magnetic Cave game!")
winsound.PlaySound(sound_file1, winsound.SND_FILENAME)
time.sleep(1)
print("Mode: Fully Manual - Easy")
winsound.PlaySound(sound_file2, winsound.SND_FILENAME)
time.sleep(1)
print("Game Rules:")
winsound.PlaySound(sound_file3, winsound.SND_FILENAME)
print("Player Black and player white move in an alternate fashion")
print("player can only place a brick on an empty cellof the cave \nprovided that the brick is stacked directly on the left or right wall, \nor is stacked to the left or the right of another brick")
print(" As soon as one player is able to align 5 consecutive bricks in a row, in a column or in a diagonal, then this\nplayer wins the game.")
winsound.PlaySound(sound_file4, winsound.SND_FILENAME)
winsound.PlaySound(sound_file5, winsound.SND_FILENAME)
input("Press Enter to start playing...")

# Main game loop
while True:
    # Create the chess board
    board = CreBoard()

    # Print the initial chess board
    PriBoard(board)

    # Define player symbols
    player1_symbol = '■'
    player2_symbol = '□'

    # Set the current player
    current_player = 1

    # Game loop
    while not BoardFull(board):
        # Get player input
        user_input = input("Player {} - Enter a position, or type 'q' to exit: ".format(current_player))

        # Check if the user wants to quit
        if user_input.lower() == 'q':
            break

        # Check if the position is valid
        if not validPos(user_input):
            print("Invalid position. Try again.")
            continue

        # Convert input to column and row indices
        column = ord(user_input[0].upper()) - ord('A')
        row = int(user_input[1]) - 1

        # Check if the position is already occupied
        if board[row][column] != '_':
            print("Position already occupied. Try again.")
            continue

        # Update the board with the player's move
        if current_player == 1:
            updBoard(board, user_input.upper(), player1_symbol)
            current_player = 2
        else:
            updBoard(board, user_input.upper(), player2_symbol)
            current_player = 1

        # Print the updated chess board
        PriBoard(board)

        # Check if the current player has won
        if win(board, player1_symbol):
            print("Player 1 wins!")
            winsound.PlaySound(sound_file6, winsound.SND_FILENAME)
            break
        elif win(board, player2_symbol):
            print("Player 2 wins!")
            winsound.PlaySound(sound_file7, winsound.SND_FILENAME)
            break

    # Check if the board is fully occupied (tie)
    if BoardFull(board):
        print("The game ends in a tie.")
        winsound.PlaySound(sound_file9, winsound.SND_FILENAME)
        

    # Ask the user if they want to restart the game
    restart = input("Do you want to restart the game? (y/n): ")
    winsound.PlaySound(sound_file8, winsound.SND_FILENAME)
    
    if restart.lower() != 'y':
        break
    print()
