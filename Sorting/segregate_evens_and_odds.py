def segregate_evens_and_odds(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    
    left = 0
    right = len(numbers)-1
    while left < right:
        while left < right and numbers[left] % 2 ==0:
            left += 1
        while left < right and numbers[right] % 2 != 0:
            right -= 1
        if left < right and numbers[left] % 2 != 0 and numbers[right] % 2 == 0:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
            right -= 1
    return numbers
