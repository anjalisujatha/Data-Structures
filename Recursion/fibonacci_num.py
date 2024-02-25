def find_fibonacci(n):
    
    return add_seq(n, 0, 1)

def add_seq(n, b1, b2):
    if n == 0:
        return b1
    else:
        return add_seq(n-1, b2, b1+b2)