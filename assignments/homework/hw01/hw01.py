"""Homework 1: Functions."""


from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:
        b = sub(0, b)
        f = add
    else:
        f = add
    return f(a, b)


def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    return add(min(max(i,j), max(j,k), max(i, k)) ** 2, min(min(i,j), min(j, k), min(i, k)) ** 2)


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factors are 1, 13
    1
    """
    #*** YOUR CODE HERE ***
    for i in range(1, n+1):
        if n % i == 0 and i != 1:
            return n//i
        elif i == n:
            return 1

def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.

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
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    #*** YOUR CODE HERE ***:
    steps = 0
    
    while 1:
        
        print(n)
        
        if n == 1:
            steps += 1
            break
        if n % 2 != 0:
            n = (n * 3) + 1
            steps += 1
        elif n % 2 == 0:
            n //= 2
            steps += 1
            
    return steps