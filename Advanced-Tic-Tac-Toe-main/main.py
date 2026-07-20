import random
def display_board(board):
    print("     0   1   2")
    print("  +---+---+---+")
    for i in range(3):
        print(f"{i} | {board[i][0]} | {board[i][1]} | {board[i][2]} |")
        print("  +---+---+---+")
    print("\n")
    
def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
    
def is_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))
    
def make_move(board, player, row, col):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        print("Square already occupied. Try again.")
        return False
def AI(board):
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    best_score = -float('inf')
    best_move = None
    for move in available_moves:
        board[move[0]][move[1]] = 'O'
        score = minimax(board, 0, False)
        board[move[0]][move[1]] = ' '  
        if score > best_score:
            best_score = score
            best_move = move
    return best_move
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif is_draw(board):
        return 0
    if is_maximizing:
        best_score = -float('inf')
        for move in [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']:
            board[move[0]][move[1]] = 'O'
            score = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ' ' 
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']:
            board[move[0]][move[1]] = 'X'
            score = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ' ' 
            best_score = min(score, best_score)
        return best_score
def play_game():
    print("Welcome to Tic Tac Toe!")
    print("1. Play against the computer")
    print("2. Play against another player")
    choice = input("Choose 1 or 2: ")

    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # X always goes first

    while True:
        display_board(board)
        if choice == '1' and current_player == 'O':
            print("Computer's turn.")
            move = AI(board)
            if move:
                make_move(board, 'O', move[0], move[1])
                if check_winner(board, 'O'):
                    display_board(board)
                    print("Computer wins!")
                    break
                if is_draw(board):
                    display_board(board)
                    print("It's a draw!")
                    break
                current_player = 'X'
            else:
                print("Error: No valid moves available.")
        else:
            print(f"Player {current_player}, it's your turn.")
            try:
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))
                if make_move(board, current_player, row, col):
                    if check_winner(board, current_player):
                        display_board(board)
                        print(f"Player {current_player} wins!")

                    if is_draw(board):
                        display_board(board)
                        print("It's a draw!")
                        break
                    current_player = 'O' if current_player == 'X' else 'X'
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column numbers between 0 and 2.")
if __name__ == "__main__":
    play_game()
    