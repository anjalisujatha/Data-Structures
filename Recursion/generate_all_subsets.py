def generate_all_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    
    result = []
    subsethelper("", s, result)
    return result
def subsethelper(slate, s, result):
    if len(s) == 0:
        result.append(slate)
    else:
        subsethelper(slate, s[1:], result)
        subsethelper(slate+s[0], s[1:], result)
        