import random
EMPTY = ' '
board = [EMPTY] * 9
def print_board(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('---------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('---------')
    print(f'{board[6]} | {board[7]} | {board[8]}')
def check_win(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)              
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)
def game_over(board):
    return check_win(board, HUMAN) or check_win(board, AI) or EMPTY not in board
def minimax(board, is_maximizing):
    if check_win(board, AI):
        return 1
    if check_win(board, HUMAN):
        return -1
    if EMPTY not in board:
        return 0
    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(board, False)
                board[i] = EMPTY
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                score = minimax(board, True)
                board[i] = EMPTY
                best_score = min(score, best_score)
        return best_score
def ai_move(board):
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = AI
def human_move(board):
    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if 0 <= move <= 8 and board[move] == EMPTY:
            board[move] = HUMAN
            break
        else:
            print("Invalid move. Try again.")
def main():
    global HUMAN, AI
    print("Welcome to Tic-Tac-Toe!")
    while True:
        player_choice = input("Do you want to be X or O? ").upper()
        if player_choice in ['X', 'O']:
            HUMAN = player_choice
            AI = 'O' if HUMAN == 'X' else 'X'
            break
        else:
            print("Invalid choice. Please choose X or O.")
    print_board(board)
    current_turn = 'X'
    while not game_over(board):
        if current_turn == HUMAN:
            human_move(board)
        else:
            ai_move(board)
        print_board(board)
        if game_over(board):
            break
        current_turn = AI if current_turn == HUMAN else HUMAN
    if check_win(board, HUMAN):
        print("Congratulations, you win!")
    elif check_win(board, AI):
        print("You lose. The AI wins!")
    else:
        print("It's a draw!")
if __name__ == "__main__":
    main()
