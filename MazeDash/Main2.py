def is_valid_move(board, x, y):
    """Check if the move is valid within the board boundaries."""
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] != 'X'

def play_game(N, M, grid, moves):
    """Play the game and determine the winner and number of moves."""
    board = [list(row) for row in grid]

    # Dynamic programming table to store minimum moves to win for each position
    dp = [[float('inf')] * N for _ in range(N)]

    # Marking destination position as 0 moves
    dp[N - 1][N - 1] = 0

    # Calculate minimum moves to reach destination for player 2 (Luigi)
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'X':
                continue
            for dx, dy in moves:
                ni, nj = i + dx, j + dy
                if is_valid_move(board, ni, nj):
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j] + 1)

    # Check if Mario can win in fewer moves than Luigi
    if dp[0][0] < float('inf'):
        return 1, dp[0][0]  # Mario wins

    return 2, float('inf')  # Luigi wins

# Example Input
test_cases = [
    (10, 2, [
        "0 X X X X X X X X X",
        "X X 0 X X X X X X X",
        "X 0 X X 0 X X X X X",
        "X X X X X X X X X X",
        "X X 0 X X 0 X X X X",
        "X X X X X X X 0 X X",
        "X X X 0 X X X X X X",
        "X X X X X X X X X X",
        "X X X X X X X X X X",
        "X X X X X X X X X X"
    ], [(2, 1), (1, 2)])
]

# Processing Input
output = []
for idx, (N, M, grid, moves) in enumerate(test_cases, start=1):
    winner, num_moves = play_game(N, M, grid, moves)
    output.append(f"Case #{idx}: {'1' if winner == 1 else '2'} {num_moves}")

# Output
for line in output:
    print(line)
