def check_if_eulerian_cycle_exists(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     bool
    """
    
    adj_list = {i: [] for i in range(n)}
    for edge in edges:
        a, b = edge
        adj_list[a].append(b)
        adj_list[b].append(a)
        
    for vertex in adj_list:
        if len(adj_list[vertex]) % 2 != 0:
            return False
            
    return True
