"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""


def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    return sorted(s0) == sorted(s1)



'''
Standard answer: 
    return set(s0) == set(s1)
'''


METADATA = {}


def check(candidate):
    assert candidate('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
    assert candidate('abcd', 'dddddddabc') == True
    assert candidate('dddddddabc', 'abcd') == True
    assert candidate('eabcd', 'dddddddabc') == False
    assert candidate('abcd', 'dddddddabcf') == False
    assert candidate('eabcdzzzz', 'dddzzzzzzzddddabc') == False
    assert candidate('aabb', 'aaccc') == False

check(same_chars)
