def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    def hflist(n, seqlen):
        print(n)
        seqlen += 1
        if n == 1:
            return seqlen
        elif n % 2 == 1:
            n = 3 * n + 1
            return hflist(n, seqlen)
        else:
            n = n // 2
            return hflist(n, seqlen)
    return hflist(n, seqlen = 0)
            
def symmetric(l):
    """Returns whether a list is symmetric. 
    >>> symmetric([])
    True
    >>> symmetric([1])
    True
    >>> symmetric([1, 4, 5, 1])
    False
    >>> symmetric([1, 4, 4, 1])
    True
    >>> symmetric(['l', 'o', 'l'])
    True
    """
    "*** YOUR CODE HERE ***"
    if (len(l) == 0) or (len(l) == 1):
        return True
    elif l[0] != l[len(l) - 1]:
        return False
    else:
        return symmetric(l[1:len(l) - 1])
        







