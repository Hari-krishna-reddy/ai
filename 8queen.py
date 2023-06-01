def solve_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        # Check if no queen is present in the same column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Check if no queen is present in the upper left diagonal
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check if no queen is present in the upper right diagonal
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def solve(row):
        if row == n:
            # Found a solution, add it to the list
            solutions.append([list(row) for row in board])
            return

        for col in range(n):
            if is_safe(row, col):
                # Place the queen and recursively solve for the next row
                board[row][col] = 1
                solve(row + 1)
                # Remove the queen (backtrack)
                board[row][col] = 0

    solve(0)
    return solutions


# Call the function to get all solutions for the 8 queens problem
solutions = solve_queens(8)

# Print the solutions
for solution in solutions:
    print("Solution:")
    for row in solution:
        print(row)
    print()
