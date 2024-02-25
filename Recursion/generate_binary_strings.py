def get_binary_strings(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """

    result = []
    bshelper("", n, result)
    return result
def bshelper(slate, n, result):
    if n == 0:
       result.append(slate)
    else:
        bshelper(slate + "0", n-1, result)
        bshelper(slate + "1", n-1, result)
        