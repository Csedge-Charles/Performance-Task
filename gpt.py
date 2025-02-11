import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def player_move(board):
    while True:
        try:
            row, col = map(int, input("Enter your move (row and column: 0 1): ").split())
            if (row, col) in get_available_moves(board):
                board[row][col] = "X"
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Enter valid row and column numbers (0-2).")

def bot_move(board):
    row, col = random.choice(get_available_moves(board))
    board[row][col] = "O"
    print(f"Bot moves to ({row}, {col})")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    
    for turn in range(9):
        if turn % 2 == 0:
            player_move(board)
        else:
            bot_move(board)
        print_board(board)
        
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            return
        elif check_winner(board, "O"):
            print("Bot wins! Better luck next time.")
            return
    
    print("It's a tie!")

if __name__ == "__main__":
    main()