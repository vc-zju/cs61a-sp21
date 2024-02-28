# Tree ADT, copy from lab05

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def change_abstraction(change):
    change_abstraction.changed = change
    
def sum_tree(t):
    """
    Add all elements in a tree.

    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    return sum([sum_tree(b) for b in branches(t)]) + label(t)

def balanced(t):
    """
    Checks if each branch has same sum of all elements,
    and each branch is balanced.

    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(t, [t, tree(1)])
    >>> balanced(t)
    False
    """
    return len(set([sum_tree(b) for b in branches(t)])) <= 1 and \
            all([balanced(b) for b in branches(t)]) 

def prune_tree(t, predicate):
    """
    Returns a new tree where any branch that has the predicate of the label
    of the branch returns True has its branches pruned.

    >>> prune_tree(tree(1, [tree(2)]), lambda x: x == 1) # prune at root
    [1]
    >>> prune_tree(tree(1, [tree(2)]), lambda x: x == 2) # prune at leaf
    [1, [2]]
    >>> prune_tree(test_tree, lambda x: x >= 3) # prune at 3, 4, and 5
    [1, [2, [4], [5]], [3]]
    >>> sum_tree(prune_tree(test_tree, lambda x: x > 10)) # prune nothing, add 1 to 9
    45
    >>> prune_tree(test_tree, lambda x: x > 10) == test_tree # prune nothing
    True
    """
    if predicate(label(t)):
        return tree(label(t))
    return tree(label(t), [prune_tree(b, predicate) for b in branches(t)])

def closest(t):
    """ Return the smallest difference between an entry and the sum of the
    root entries of its branches .
    >>> t = tree(8 , [tree(4), tree(3)])
    >>> closest(t) # |8 - (4 + 3)| = 1
    1
    >>> closest(tree(5, [t])) # Same minimum as t
    1
    >>> closest(tree(10, [tree(2), t])) # |10 - (2 + 8)| = 0
    0
    >>> closest(tree(3)) # |3 - 0| = 3
    3
    >>> closest(tree(8, [tree(3, [tree(1, [tree(5)])])])) # 3 - 1 = 2
    2
    >>> sum([])
    0
    """
    diff = abs(label(t) - sum([label(b) for b in branches(t)]))
    return min([closest(b) for b in branches(t)] + [diff])

def dejavu(t, n):
    """
    >>> my_tree = tree(2, [tree(3, [tree(5), tree(7)]), tree(4)])
    >>> dejavu(my_tree, 12) # 2 -> 3 -> 7
    True
    >>> dejavu(my_tree, 5) # Sums of partial paths like 2 -> 3 don ’t count
    False
    """
    if is_leaf(t):
        return n == label(t)
    for b in branches(t):
        if dejavu(b, n - label(t)):
            return True
    return False

def reduce(f, s, initial):
    """Combine elements of s pairwise
    using f, starting with initial.

    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(pow, [2, 3, 1], 2)
    64
    """
    for x in s:
        initial = f(initial, x)
    return initial

# The one function defined below is used in the questions below 
# to convert truthy and falsy values into the numbers 1 and 0, respectively.
def one(b):
    if b:
        return 1
    else:
        return 0

def bigpath(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigpath(t, 3)
    3
    >>> bigpath(t, 6)
    2
    >>> bigpath(t, 9)
    1
    """
    if is_leaf(t):
        return one(n <= label(t))
    return sum([bigpath(b, n - label(t)) for b in branches(t)])

def allpath(t, f, g, s):
    """ Return the number of paths p in t for which f(reduce(g, p, s)) is truthy.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> even = lambda x: x % 2 == 0
    >>> allpath(t, even, max, 0) # Path maxes are 2, 4, and 5
    2
    >>> allpath(t, even, pow, 2) # E.g., pow(pow(2, 1), 2) is even
    3
    >>> allpath(t, even, pow, 1) # Raising 1 to any power is odd
    0
    """
    if is_leaf(t):
        return one(f(g(s, label(t))))
    return sum([allpath(b, f, g, g(s, label(t))) for b in branches(t)])

from operator import add , mul

def bigpath_allpath(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigpath_allpath(t, 3)
    3
    >>> bigpath_allpath(t, 6)
    2
    >>> bigpath_allpath(t, 9)
    1
    """
    return allpath(t, lambda x: x >= n, add, 0)
