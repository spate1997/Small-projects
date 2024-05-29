from IPython.display import clear_output

# Initialize the board
def initialize_board():
    return [' '] * 10  # We'll use indices 1-9 for simplicity

# Function to print the board
def print_board(board):
    clear_output()  # Clear the output for Jupyter Notebook
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

# Function to take player input and place their marker on the board
def player_input(board, marker):
    position = input(f"Player {marker}, choose your position: (1-9) ")
    while not position.isdigit() or int(position) not in range(1, 10) or board[int(position)] != ' ':
        position = input("Invalid position. Choose another position: (1-9) ")
    board[int(position)] = marker

# Function to check if a player has won the game
def check_win(board, marker):
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

# Function to check if the game is a tie
def check_tie(board):
    return ' ' not in board[1:]  # Check if there's no empty space left

# Main game loop
def play_game():
    print("Welcome to Tic Tac Toe!")
    board = initialize_board()
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
        play_game()

# Start the game
play_game()


# Start the game
play_game()
