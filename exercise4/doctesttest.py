def factorial(n):
    """
    :param n:
    :return:
    >>> factorial(1)
    1
    >>> factorial(2)
    3
    >>> factorial(5)
    120
    """
    num = 1
    while n > 1:
        num *= n
        n -= 1
    return num

if __name__ == '__main__':
    import doctest
    doctest.testmod()
