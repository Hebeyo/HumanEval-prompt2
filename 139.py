"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""

def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    fact = 1
    special_fact = 1
    for i in range(1, n+1):
        fact *= i
        special_fact *= fact
    return special_fact



'''
Standard answer: 
    fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact
'''
def check(candidate):

    # Check some simple cases
    assert candidate(4) == 288, "Test 4"
    assert candidate(5) == 34560, "Test 5"
    assert candidate(7) == 125411328000, "Test 7"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1) == 1, "Test 1"

check(special_factorial)
