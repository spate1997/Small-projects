from IPython.display import clear_output
# Initialize the board
board = [' '] * 10  # We'll use indices 1-9 for simplicity

def print_board(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def player_input(board, marker):
    position = int(input(f"Player {marker}, choose your position: (1-9) "))
    while board[position] != ' ':
        position = int(input("Position already taken, choose another position: (1-9) "))
    board[position] = marker

def check_win(board, marker):
    # Check all win conditions
    win_conditions = [
        (board[7] == board[8] == board[9] == marker),  # top row
        (board[4] == board[5] == board[6] == marker),  # middle row
        (board[1] == board[2] == board[3] == marker),  # bottom row
        (board[7] == board[4] == board[1] == marker),  # left column
        (board[8] == board[5] == board[2] == marker),  # middle column
        (board[9] == board[6] == board[3] == marker),  # right column
        (board[7] == board[5] == board[3] == marker),  # diagonal
        (board[9] == board[5] == board[1] == marker)   # diagonal
    ]
    return any(win_conditions)

def check_tie(board):
    return ' ' not in board[1:]  # Check if there's no empty space left

def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    
    game_on = True
    current_marker = 'X'
    
    while game_on:
        player_input(board, current_marker)
        print_board(board)
        
        if check_win(board, current_marker):
            print(f"Player {current_marker} wins!")
            game_on = False
        elif check_tie(board):
            print("The game is a tie!")
            game_on = False
        else:
            # Switch player
            current_marker = 'O' if current_marker == 'X' else 'X'
    
    if input("Do you want to play again? (yes/no): ").lower().startswith('y'):
        # Reset the board and start again
        global board
        board = [' '] * 10
        play_game()

# Start the game
play_game()
