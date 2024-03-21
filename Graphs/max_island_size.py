def max_island_size(grid):
    """
    Args:
     grid(list_list_int32)
    Returns:
     int32
    """
    
    if not grid or not grid[0]:
        return 0
    
    n = len(grid)
    m = len(grid[0])
    max_island_size = 0
    
    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != 1:
            return 0
            
        grid[x][y] = 0
        island_size = 1
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            island_size += dfs(new_x, new_y)
        return island_size
        
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                island_size = dfs(i, j)
                max_island_size = max(max_island_size, island_size)
                
    return max_island_size
