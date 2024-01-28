def is_palindrome(s):
    """
    >>> is_palindrome("tenet")
    True
    >>> is_palindrome("tenets")
    False
    >>> is_palindrome("raincar")
    False
    >>> is_palindrome("")
    True
    >>> is_palindrome("a")
    True
    >>> is_palindrome("ab")
    False
    """
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

def greatest_pal(s):
    """
    >>> greatest_pal("tenet")
    'tenet'
    >>> greatest_pal("tenets")
    'tenet'
    >>> greatest_pal("stennet")
    'tennet'
    >>> greatest_pal("25 racecars")
    'racecar'
    >>> greatest_pal("abc")
    'a'
    >>> greatest_pal("")
    ''
    """
    if is_palindrome(s):
        return s
    left, right = greatest_pal(s[:-1]), greatest_pal(s[1:])
    if len(left) >= len(right):
        return left
    return right

# def greatest_pal(s):
#     """
#     >>> greatest_pal("tenet")
#     'tenet'
#     >>> greatest_pal("tenets")
#     'tenet'
#     >>> greatest_pal("stennet")
#     'tennet'
#     >>> greatest_pal("25 racecars")
#     'racecar'
#     >>> greatest_pal("abc")
#     'a'
#     >>> greatest_pal("")
#     ''
#     """
#     def helper(a, b, c):
#         if __________________________ > ____________________________:
#             return _______________________________________________
#         elif ________________________ > ____________________________:
#             return _______________________________________________
#         elif ________________ and _______________________________
#             ______________________________________________________
#         return ____________________________________________________
#     return helper(1, 0, "")

# def greatest_pal(s):
#     """
#     >>> greatest_pal("tenet")
#     'tenet'
#     >>> greatest_pal("tenets")
#     'tenet'
#     >>> greatest_pal("stennet")
#     'tennet'
#     >>> greatest_pal("25 racecars")
#     'racecar'
#     >>> greatest_pal("abc")
#     'a'
#     >>> greatest_pal("")
#     ''
#     """
#     def helper(a, b):
#         if ______________________________________________________:
#             return ______________________________________________________
#         elif ______________________________________________________:
#             return ______________________________________________________
#         return ______________________________________________________
#     return _________________________________________________________________

# def greatest_pal_two(s):
#     """
#     >>> greatest_pal_two("tenet")
#     'tenet'
#     >>> greatest_pal_two("tenets")
#     'tenet'
#     >>> greatest_pal_two("stennet")
#     'tennet'
#     >>> greatest_pal_two("abc")
#     'a'
#     >>> greatest_pal_two("")
#     ''
#     """
#     for _____ in __________________________________________________________:
#         if ________________________________________________________________________:
#             return  ________________________________________________________________________
#     return s

# Y = lambda f: (lambda x: x(x))(lambda x: f(lambda z: x(x)(z)))
# fib_maker = lambda f: lambda r: ________________________________________________________________
# is_pal_maker = lambda f: lambda r: _____________________________________________________________

# fib = Y(fib_maker)
# is_pal = Y(is_pal_maker)

# # This code sets up doctests for fib and is_pal. Run test(fib) and test(is_pal) to check your implementation

# fib.__name__ = 'fib'
# fib.__doc__="""Given n, returns the nth Fibonacci nuimber.

# >>> fib(0)
# 0
# >>> fib(1)
# 1
# >>> fib(2)
# 1
# >>> fib(3)
# 2
# >>> fib(4)
# 3
# >>> fib(5)
# 5
# """

# is_pal.__name__ = 'is_pal'
# is_pal.__doc__="""Returns whether or not an input string s is a palindrome.

# >>> is_pal('tenet')
# True
# >>> is_pal('tenets')
# False
# >>> is_pal('ab')
# False
# >>> is_pal('')
# True
# >>> is_pal('a')
# True
# """