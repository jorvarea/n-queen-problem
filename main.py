from print_board import print_board

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

def valid_state(board: list[list[int]]) -> bool:
    

def solve_n_queens(board: list[list[int]], num_queens: int) -> None:


def main() -> None:
    size, num_queens = read_input()
    board = [[0 for _ in range(size)] for _ in range(size)]
    print_board(board)

if __name__ == "__main__":
    main()
