def fib(n):
    """
    This fuction calculates Fibonnacci sequence
    n -- 
    Returns: int -- 
    """
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(3))
