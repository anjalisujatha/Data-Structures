def count_islands(matrix):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     int32
    """
    
    if not matrix or not matrix[0]:
        return 0
        
    
    n = len(matrix)
    m = len(matrix[0])
    islands = 0
    
    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= m or matrix[x][y] != 1:
            return 
        matrix[x][y] = 0
        directions = [(1,0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            dfs(new_x, new_y)
        
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                islands += 1
                dfs(i, j)
    return islands
        