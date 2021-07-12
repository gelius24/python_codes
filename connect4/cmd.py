import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7


def print_board(board):
    print(np.flip(board, 0))


def create_board():
    game_board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return game_board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True


board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    # Ask Player 1 input
    if turn == 0:
        col = int(input("Joueur 1 Joue (0-6) "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
        if winning_move(board, col):
            print("Player 1 Wins !!!! Congrats!")
            game_over = True

    else:
        col = int(input("Joueur 2 Joue (0-6) "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            if winning_move(board, col):
                print("Player 2 Wins !!!! Congrats!")
                game_over = True
    print_board(board)
    turn += 1
    turn %= 2
