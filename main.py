from variable_class import Variable
from board import print_board, fill_board
from backtracking import solve_n_queens

def read_input() -> tuple[int, int]:
    done = False
    while not done:
        try:
            size = int(input("Please enter the size of the board: "))
            if size <= 0:
                raise ValueError("The size of the board should be greater than 0")
            num_queens = int(input("Please enter the number of queens to place: "))
            if num_queens <= 0:
                raise ValueError("The number of queens should be greater than 0")
            done = True
        except ValueError as exc:
            print(f"Error: {exc!r}")
            done = False
    return size, num_queens

def main() -> None:
    size, num_queens = read_input()
    variables = [Variable(-1, set(num for num in range(size))) for _ in range(size)]
    result = solve_n_queens(variables, num_queens)
    if result:
        board = fill_board(result, size)
        print_board(board)
    else:
        print("Problem impossible to solve")

if __name__ == "__main__":
    main()
