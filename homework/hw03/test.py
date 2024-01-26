def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """
    if change < 0:
        return 0
    if change == 0:
        return 1
    v = count_coins(change - 1) + count_coins(change - 5) \
        + count_coins(change - 10) + count_coins(change - 25)
    print(change, v)
    return v

count_coins(6)
