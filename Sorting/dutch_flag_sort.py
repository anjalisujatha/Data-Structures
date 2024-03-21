def dutch_flag_sort(balls):
    """
    Args:
     balls(list_char)
    Returns:
     list_char
    """
    
    left = 0
    right = len(balls) - 1
    current = 0
    
    while current <= right:
        if balls[current] == 'R':
            balls[left], balls[current] = balls[current], balls[left]
            left += 1
            current += 1
        elif balls[current] == 'B':
            balls[right], balls[current] = balls[current], balls[right]
            right -= 1
        else:
            current += 1
    return balls
