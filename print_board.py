from config import BG_BLUE, BG_CYAN, WHITE, RESET, QUEEN_ICON

def print_board(board: list[list[int]]):
    for i in range(len(board)):
            for j in range(len(board)):
                bg_color = BG_CYAN if (i + j) % 2 == 0 else BG_BLUE
                piece_icon = QUEEN_ICON if board[i][j] == 1 else ' '
                print(f"{bg_color}{WHITE} {piece_icon} {RESET}", end='')
            print()
