def two_sum(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    
    my_dict = {}
    for indx, ele in enumerate(numbers):
        num = target - ele
        if num in my_dict:
            return [my_dict[num], indx]
        else:
            my_dict[ele] = indx
    return [-1, -1]

