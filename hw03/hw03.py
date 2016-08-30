HW_SOURCE_FILE = 'hw03.py'

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

    
    
def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    glist = [1, 2, 3]
    for i in range(3, n):
        atom = glist[i - 1] + 2 * glist[i - 2] + 3 * glist[i - 3]
        glist.append(atom)
    return glist[n - 1]             

        

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def upordown(n):
        '''
        n - 1 to n True for plus one True for plus one
        '''
        if n == 2:
            return True
        elif (n - 1) % 7 == 0:
            return not upordown(n - 1)
        elif has_seven(n - 1):
            return not upordown(n - 1)
        else:
            return upordown(n - 1)
    
    if n == 1:
        return 1
    elif upordown(n):
        return pingpong(n - 1) + 1
    else:
        return pingpong(n - 1) - 1
        

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
        
        
        


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"

def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    "*** YOUR CODE HERE ***"
    listcheck = [type(atom) for atom in lst]
    if list in listcheck:
        p = listcheck.index(list)
        return lst[:p] + flatten(lst[p]) + flatten(lst[p + 1:])
    else:
        return lst

def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    if lst1 == []:    
        return lst2
    elif lst2 ==[]:
        return lst1
    elif lst1[0] <= lst2[0]:
        return lst1[:1] + merge(lst1[1:], lst2)
    else:
        return lst2[:1] + merge(lst1, lst2[1:])
    
def mergesort(seq):
    """Mergesort algorithm.

    >>> mergesort([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort([])     # sorting an empty list
    []
    >>> mergesort([1])   # sorting a one-element list
    [1]
    """
    "*** YOUR CODE HERE ***"   
    if len(seq) == 1:
        return seq    
    elif len(seq) == 2:
        return merge(seq[:1], seq[1:])
    else:
        return merge(mergesort(seq[:int(len(seq) // 2)]),
                     mergesort(seq[int(len(seq) // 2):])
                    )
    
###################
# Extra Questions #
###################

from operator import sub, mul

def Y(f):
    """The Y ("paradoxical") combinator."""
    return f(lambda: Y(f, n))


def Y_tester():
    """
    >>> tmp = Y_tester()
    >>> tmp(1)
    1
    >>> tmp(5)
    120
    >>> tmp(2)
    2
    """
    "*** YOUR CODE HERE ***"
    return Y(lambda f: lambda x: 1 if x == 1 else x * f(x - 1))  # Replace 
 
def make_anonymous_factorial():
    return (lambda f: lambda n: f(f, n))(lambda f, n: 1 if n == 1 else mul(n, f(f, sub(n, 1))))


# return Y(lambda: lambda x: 1 if x == 1 else mul(x, (sub(x, 1))))  # Replace 

# >>> fact = lambda n: 1 if n == 1 else mul(n, fact(sub(n, 1)))

tmp = Y_tester()

print(tmp(1))
#print(tmp(2))



'''


where ? is an expression containing only lambda expressions, 
conditional expressions, function calls, and the functions mul and sub. 
That is, ? contains no statements 
(no assignments or def statements in particular), 
and no mention of fact or any other identifier defined outside ? 
other than mul or sub from the operator module. 
You are also allowed to use the equality (==) operator. 

Find such an expression to use in place of ?.

'''



