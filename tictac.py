def check_winner(board):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None


def print_board(board):
    print('---------')
    for i in range(3):
        print('|', end='')
        for j in range(3):
            print(board[i][j], end='|')
        print('\n---------')


def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)

        row = int(input(f"Player {player}, enter the row (0-2): "))
        col = int(input(f"Player {player}, enter the column (0-2): "))

        if board[row][col] == ' ':
            board[row][col] = player
        else:
            print("That position is already occupied. Try again.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Check for a tie
        if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            print_board(board)
            print("It's a tie!")
            break

        player = 'O' if player == 'X' else 'X'


play_game()
