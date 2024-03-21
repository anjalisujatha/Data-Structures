def find_fibonacci(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    
    if n == 0 or n == 1:
        return n
        
    table = [0]*3
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i%3] = table[(i-1)%3] + table[(i-2)%3]
    return table[n%3]
