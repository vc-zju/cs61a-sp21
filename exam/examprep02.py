def match_k(k):
    """ Return a function that checks if digits k apart match

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def do_match(x):
        while x >= 10 ** k:
            if x % 10 != (x // (10 ** k)) % 10:
                return False
            x //= 10
        return True
    return do_match

def chain_function():
    """
    >>> tester = chain_function()
    >>> x = tester(1)(2)(4)(5) # Expected 3 but got 4, so print 3. 1st chain break, so print 1 too.
    3 1
    >>> x = x(2) # 6 should've followed 5 from above, so print 6. 2nd chain break, so print 2
    6 2
    >>> x = x(8) # The chain restarted at 2 from the previous line, but we got 8. 3rd chain break.
    3 3
    >>> x = x(3)(4)(5) # Chain restarted at 8 in the previous line, but we got 3 instead. 4th break
    9 4
    >>> x = x(9) # Similar logic to the above line
    6 5
    >>> x = x(10) # Nothing is printed because 10 follows 9.
    >>> y = tester(4)(5)(8) # New chain, starting at 4, break at 6, first chain break
    6 1
    >>> y = y(2)(3)(10) # Chain expected 9 next, and 4 after 10. Break 2 and 3.
    9 2
    4 3
    """
    def g(x, y):
        def h(n):
            if x <= 0 or n == x + 1:
                return g(n, y)
            else:
                print(x + 1, y)
                return g(n, y + 1)
        return h
    return g(0, 1)

def cs61nay(combiner, n):
    """ Return a function that takes n arguments,
    one at a time, and combines them using combiner.

    >>> f = cs61nay(lambda x, y: x * y, 3)
    >>> f(2)(3)(4) # 2 * 3 * 4
    24
    >>> f(-1)(2)(3) # -1 * 2 * 3
    -6
    >>> f = cs61nay(lambda x, y: x - y, 4)
    >>> f(1)(2)(-2)(-1) # 1 - 2 - -2 - -1
    2
    >>> f = cs61nay(lambda x, y: x + y, 1)
    >>> f(61)
    61
    >>> f(2021)
    2021
    """
    if n == 1:
        return lambda x: x
    else:
        return lambda x: lambda y: cs61nay(combiner, n - 1)(combiner(x, y))
    
from operator import sub, add, mul

compose = lambda f, g: lambda x: f(g(x))

print(compose(cs61nay(sub, 2), compose(cs61nay(mul, 3)(2),
      cs61nay(pow, 2)(10))(3))(1)(-21))

cs61NAY = lambda combiner, n: (n == 1 and (lambda x: x)) or (lambda x: lambda y: cs61NAY(combiner, n - 1)(combiner(x, y)))

# This syntax adds a doctest to a lambda, which can be run using `test(cs61NAY)`
# after clicking Run in 61A Code or `python3 -m doctest -v examprep02.py`
# if you save the questions to a .py file
cs61NAY.__name__ = "cs61NAY"
cs61NAY.__doc__ = """ Return a function that takes n arguments,
    one at a time, and combines them using combiner.

    >>> f = cs61NAY(lambda x, y: x * y, 3)
    >>> f(2)(3)(4) # 2 * 3 * 4
    24
    >>> f(-1)(2)(3) # -1 * 2 * 3
    -6
    >>> f = cs61NAY(lambda x, y: x - y, 4)
    >>> f(1)(2)(-2)(-1) # 1 - 2 - -2 - -1
    2
    >>> f = cs61NAY(lambda x, y: x + y, 1)
    >>> f(61)
    61
    >>> f(2021)
    2021
    """
    
def stacklist():
    """
    >>> append, get = stacklist()
    >>> get, y = append(2)
    >>> get, y = append(3, get, y)
    >>> get, y = append(4, get, y)
    >>> get(0)
    2
    >>> get(1)
    3
    >>> get(2)
    4
    >>> get, y = append(8, get, y)
    >>> get(1)
    3
    >>> get(3)
    8
    """
    g = lambda i: "Error: out of bounds!"
    def f(value, g=g, y=0):
        h = g
        def g(i):
            if i == y:
                return value
            return h(i)
        return g, y + 1
    return f, g

def stacklisted():
    """
    >>> append, get, insert = stacklisted()
    >>> get, idx = append(2)
    >>> get, idx = append(13, get, idx)
    >>> get, idx = append(4, get, idx)
    >>> get, idx = insert(1, 19, get, idx)
    >>> get(0)
    2
    >>> get(1)
    19
    >>> get(2)
    13
    >>> get(3)
    4
    """
    g = lambda i: "Error: out of bounds!"
    def f(value, g=g, y=0):
        h = g
        def g(i):
            if i == y:
                return value
            return h(i)
        return g, y + 1

    def h(y, value, g, n):
        e = g
        def g(i):
            if i == y:
                return value
            return e(i)
        k = y
        while k < n:
            g, ret = f(e(k), g, k + 1)
            k += 1
        return g, ret
    return f, g, h