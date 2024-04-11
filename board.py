from config import BG_BLUE, BG_CYAN, WHITE, RESET, QUEEN_ICON
from variable_class import Variable

def fill_board(variables: list[Variable], size: int) -> list[list[int]]:
    board = [[0 for _ in range(size)] for _ in range(size)]
    for column, var in enumerate(variables):
        if var.value != -1:
            board[var.value][column] = 1
    return board

def print_board(board: list[list[int]]):
    for i in range(len(board)):
        for j in range(len(board)):
            bg_color = BG_CYAN if (i + j) % 2 == 0 else BG_BLUE
            piece_icon = QUEEN_ICON if board[i][j] == 1 else ' '
            print(f"{bg_color}{WHITE} {piece_icon} {RESET}", end='')
        print()
