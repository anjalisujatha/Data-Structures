def tower_of_hanoi(n):
    """
    Args:
     n(int32)
    Returns:
     list_list_int32
    """
    
    result = []
    def transfer_disk(n, source, destination, auxiliary):
        if n == 1:
            result.append([source, destination])
        else:
            transfer_disk(n-1, source, auxiliary, destination)
            result.append([source, destination])
            transfer_disk(n-1, auxiliary, destination, source)
            
    transfer_disk(n, 1, 3, 2)
    return result
