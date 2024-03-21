def check_if_eulerian_path_exists(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     bool
    """

    adj_list = {i: [] for i in range(n)}
    for edge in edges:
        a,b = edge
        adj_list[a].append(b)
        adj_list[b].append(a)
        
    odd_count = 0
    for vertex in adj_list:
        if len(adj_list[vertex]) % 2 != 0:
            odd_count += 1
            
    if odd_count == 0 or odd_count == 2:
        return True
    else:
        return False

