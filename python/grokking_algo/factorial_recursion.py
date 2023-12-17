def get_factorial(n):
    """
    Takes n as input and return n!
    """
    if n <= 1:
        return 1
    else:
        # print(n)
        return n * get_factorial(n-1)
