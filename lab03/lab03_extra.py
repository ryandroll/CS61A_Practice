from lab03 import *

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2  * 0
    0
    """
    if n == 0:
        return 0
    else:
        return n * skip_mul(n - 2)

def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def counter(i):
        "*** YOUR CODE HERE ***"
        
        

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if a < b:
        return gcd(b, a)
    elif a % b != 0:
        return gcd(b, a % b)
    else:
        return b
        


def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    "*** YOUR CODE HERE ***"
    return a * b + c
    
    

def has_sublist(l, sublist):
    """Returns whether the elements of sublist appear in order anywhere within list l.
    >>> has_sublist([], [])
    True
    >>> has_sublist([3, 3, 2, 1], [])
    True
    >>> has_sublist([], [3, 3, 2, 1])
    False
    >>> has_sublist([3, 3, 2, 1], [3, 2, 1])
    True
    >>> has_sublist([3, 2, 1], [3, 2, 1])
    True
    """
    sublist_length = len(sublist)
    l_length = len(l)
    "*** YOUR CODE HERE ***"    
    if l_length <= sublist_length:
        return l == sublist
    elif l[:len(sublist)] == sublist:
        return True
    else:
        return has_sublist(l[1:], sublist)
        
def remove_first(lst, elem):
    """ This function removes the first appearance of elem in list lst.

    >>> remove_first([3, 4] , 3)
    [4]
    >>> remove_first([3, 4, 3] , 3)
    [4, 3]
    >>> remove_first([2, 4] , 3)
    [2, 4]
    >>> remove_first([] , 0)
    []
    """
    "*** YOUR CODE HERE ***"
    if lst == []:
        return []
    elif lst[0] == elem:
        return lst[1:]
    else:
        return lst[:1] + remove_first(lst[1:], elem)
        

def sort(lst):
    """This function returns a sorted version of the list lst.

    >>> sort([6, 2, 5])
    [2, 5, 6]
    >>> sort([2, 3])
    [2, 3]
    >>> sort([3])
    [3]
    >>> sort([])
    []
    """ 
    "*** YOUR CODE HERE ***"
    if len(lst) <= 1:
        return lst
    else:
        return [min(lst)] + sort(remove_first(lst, min(lst)))        
        
def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    def allodd(n):
        if n == 1:
            return odd_term(1)
        else:
            return odd_term(n) + alleven(n - 1)
    def alleven(n):
        if n == 0:
            return 0
        else: 
            return even_term(n) + allodd(n - 1)
    if n % 2 == 0:
        return alleven(n)
    else:
        return allodd(n)

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    else:
        return ten_pairs(n//10) + count_digit(n//10, 10 - n%10)

def count_digit(n, digit):
    """Return how many times digit appears in n.

    >>> count_digit(55055, 5)
    4
    """
    if n == 0:
        return 0
    else:
        if n%10 == digit:
            return count_digit(n//10, digit) + 1
        else:
            return count_digit(n//10, digit)

    
    
def is_prime(n):
    """Returns True if n is a prime number and False otherwise. 

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    from math import sqrt
    def checking(i, n):
        if i == 1:
            return True
        elif n % i == 0 and i > 1:
            return False
        else:
            return checking(i - 1, n)
    return False if n == 1 else checking(int(sqrt(n)), n)
        
        
    