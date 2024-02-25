MOD = 10**9 + 7
def calculate_power(a, b):
    """
    Args:
     a(int64)
     b(int64)
    Returns:
     int32
    """
    # Write your code here.
    if b == 0:
        return 1
    elif b == 1:
        return a % MOD
    half_power = calculate_power(a, b//2) % MOD
    result = (half_power * half_power) % MOD
    if b % 2 == 0:
        return result
    else:
        return (a * result) % MOD
        