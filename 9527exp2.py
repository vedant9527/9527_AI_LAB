#vedant chawardol 9527 magic square method
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    magic_square = [[8, 1, 6],
                    [3, 5, 7],
                    [4, 9, 2]]

    print("Welcome to Magic Square Tic Tac Toe!")
    print_board(board)

    while True:
        print(f"Magic Square for reference:")
        print_board([[str(cell) for cell in row] for row in magic_square])

        row = int(input(f"Player {current_player}, enter row (0, 1, or 2) corresponding to the magic square: "))
        col = int(input(f"Player {current_player}, enter column (0, 1, or 2) corresponding to the magic square: "))

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Cell already occupied. Try again.")
            continue

        print_board(board)

        if is_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
