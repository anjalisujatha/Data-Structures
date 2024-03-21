def ncr(n, r):
    """
    Args:
     n(int32)
     r(int32)
    Returns:
     int32
    """
    
    MOD = 10 ** 9 + 7
    if r == 0 or r == n:
        return 1
    if r > n:
        return 0
    table = [[0] * (r+1) for _ in range(n+1)]
    for row in range(n+1):
        table[row][0] = 1
    for col in range(r+1):
        table[col][col] = 1
    for row in range(2, n+1):
        for col in range(1, min(row,r)+1):
            table[row][col] = (table[row-1][col] + table[row-1][col-1]) % MOD
    return table[n][r]
