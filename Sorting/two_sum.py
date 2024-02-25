def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    leftindx = 0
    rightindx = len(numbers) -1
    while leftindx < rightindx:
        sum = numbers[leftindx] + numbers[rightindx]
        if sum == target:
            return [leftindx, rightindx]
        else:
            if sum > target:
                rightindx -= 1
            else: 
                leftindx += 1
    return [-1, -1]
