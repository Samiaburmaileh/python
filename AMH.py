# Sami Abu Rmaileh & Malak Raddad 
# ID : 1192325 & ID : 1192408
# We certify that this submission is the original work of members of the group and meets
# the Faculty's Expectations of Originality# Expectations of Originality
# we start the project in 12/5/2023 friday 

import random
import time 
import winsound
sound_file1 = "sounds\Welcome.wav"
sound_file2 = "sounds\Mhard.wav"
sound_file3 = "sounds\Rules.wav"
sound_file4 = "sounds\gameruls.wav"
sound_file5 = "sounds\Enter.wav"
sound_file6 = "sounds\White.wav"
sound_file7 = "sounds\AIwin.wav"
sound_file8 = "sounds\Tie.wav"
sound_file9 = "sounds\Restart.wav"
sound_file19 = "sounds\playerone.wav"

def CreBoard():
    board = []
    for _ in range(8):
        row = ['_'] * 8
        board.append(row)
    return board


def PriBoard(board):
    print("    A B C D E F G H     ")
    for i in range(8, 0, -1):
        row_str = f"{i} │ "
        for j in range(8):
            row_str += board[i-1][j] + " "
        row_str += "│"
        print(row_str)
    print("    A B C D E F G H     ")


def updBoard(board, position, symbol):
    column = ord(position[0].upper()) - ord('A')
    row = int(position[1]) - 1

    # Check if the position is valid
    if not validPos(position):
        print("Invalid position. Try again.")
        return False

    # Check if the position is already occupied
    if board[row][column] != '_':
        print("Position already occupied. Try again.")
        return False

    # Check if the position is valid
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

    # Update the board with the player's move
    board[row][column] = symbol
    return True


def BoardFull(board):
    for row in board:
        if '_' in row:
            return False
    return True


def validPos(position):
    if len(position) != 2:
        return False
    column = position[0].upper()
    row = position[1]
    return column in 'ABCDEFGH' and row in '12345678'


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


def ai_hard(board, player_symbol, ai_symbol):
    empty_positions = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == '_':
                empty_positions.append((i, j))

    # Check if the player is one move away from winning
    for position in empty_positions:
        row, col = position
        board[row][col] = player_symbol
        if win(board, player_symbol):
            board[row][col] = '_'
            return position
        board[row][col] = '_'

    # Choose a random valid position if no winning move is found
    valid_positions = []
    for position in empty_positions:
        row, col = position
        if (col == 0 or board[row][col - 1] != '_') or (col == 7 or board[row][col + 1] != '_'):
            valid_positions.append(position)

    if valid_positions:
        return random.choice(valid_positions)
    else:
        return random.choice(empty_positions)


# Function to restart the game
def restart_game():
    print("Restarting the game...")
    print()


# Main game loop
print("Welcome to the Magnetic Cave game!")
winsound.PlaySound(sound_file1, winsound.SND_FILENAME)
time.sleep(1)
print("Mode: Single Player - Hard")
winsound.PlaySound(sound_file2, winsound.SND_FILENAME)
time.sleep(1)
print("Manual entry for white's moves & automatic moves for blacks\nAI starts the first move.")
winsound.PlaySound(sound_file6, winsound.SND_FILENAME)
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

    # Define player and AI symbols
    player_symbol = '□'
    ai_symbol = '■'

    # Set the current player
    current_player = 1

    # Game loop
    while not BoardFull(board):
        # AI turn 
        if current_player == 1:
            ai_move = ai_hard(board, player_symbol, ai_symbol)
            row, col = ai_move
            position = chr(col + ord('A')) + str(row + 1)
            print("AI chooses position:", position)

            # Update the board with the AI's move
            if updBoard(board, position, ai_symbol):
                current_player = 2
                PriBoard(board)

            # Check if the AI has won
            if win(board, ai_symbol):
                print("AI wins!")
                winsound.PlaySound(sound_file7, winsound.SND_FILENAME)
                break

        # player turn 
        else:
            # Get player input
            start_time = time.time()

            user_input = input("Player - Enter a position, or type 'q' to exit: ")

            # Check if the user wants to quit
            if user_input.lower() == 'q':
                break
        # Calculate elapsed time
            elapsed_time = time.time() - start_time

        # Check if the player ran out of time
            if elapsed_time >= 3:
                print("Time's up! Next player's turn.")
                current_player = 1
                continue

            # Check if the position is valid
            if not validPos(user_input):
                print("Invalid position. Try again.")
                current_player = 1
                continue

            # Update the board with the player's move
            if updBoard(board, user_input.upper(), player_symbol):
                current_player = 1
                PriBoard(board)

                # Check if the player has won
                if win(board, player_symbol):
                    print("Player wins!")
                    winsound.PlaySound(sound_file19, winsound.SND_FILENAME)
                    break

    # Check if the board is fully occupied (tie)
    if BoardFull(board):
        print("The game ends in a tie.")
        winsound.PlaySound(sound_file8, winsound.SND_FILENAME)

    # Ask the user if they want to restart the game
    restart = input("Do you want to restart the game? (y/n): ")
    winsound.PlaySound(sound_file9, winsound.SND_FILENAME)
    if restart.lower() != 'y':
        break
    print()
