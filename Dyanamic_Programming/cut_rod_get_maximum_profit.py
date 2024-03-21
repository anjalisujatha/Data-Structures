def get_maximum_profit(price):
    """
    Args:
     price(list_int32)
    Returns:
     int32
    """
   
    n = len(price)
    result = [0] * (n+1)
    
    for rodsize in range(1, n+1):
        result[rodsize] = 0
        for cutsize in range(1, rodsize+1):
            result[rodsize] = max(price[cutsize-1]+result[rodsize-cutsize], result[rodsize])
            
    return result[n]

