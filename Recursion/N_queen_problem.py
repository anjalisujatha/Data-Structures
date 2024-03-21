def find_all_arrangements(n):
    """
    Args:
     n(int32)
    Returns:
     list_list_str
    """

    def is_valid(board, row, col):
        for i in range(row):
            if board[i][col] == 'q':
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'q':
                return False
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 'q':
                return False
        return True
    def backtrack(board, row):
        if row == n:
            result.append(["".join(row) for row in board])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row][col] = 'q'
                backtrack(board, row+1)
                board[row][col] = "-"
            
    result = []
    board = [["-" for _ in range(n)] for _ in range(n)]
    backtrack(board, 0)
    return result
    