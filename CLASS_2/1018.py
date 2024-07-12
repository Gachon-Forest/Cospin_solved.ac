def count_repaints(board, start_row, start_col, pattern):
    count = 0
    for i in range(8):
        for j in range(8):
            if board[start_row + i][start_col + j] != pattern[i][j]:
                count += 1
    return count

row_n, col_n = map(int, input().split())
board = []
for _ in range(row_n):
    board.append(list(input()))

w_board = [
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
]

b_board = [
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
]

min_repaints = float('inf')

for i in range(row_n - 7):
    for j in range(col_n - 7):
        w_count = count_repaints(board, i, j, w_board)
        b_count = count_repaints(board, i, j, b_board)
        min_repaints = min(min_repaints, w_count, b_count)

print(min_repaints)
