"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    result = []
    for number in numbers.split(' '):
        if number == 'zero':
            result.append(0)
        elif number == 'one':
            result.append(1)
        elif number == 'two':
            result.append(2)
        elif number == 'three':
            result.append(3)
        elif number == 'four':
            result.append(4)
        elif number == 'five':
            result.append(5)
        elif number == 'six':
            result.append(6)
        elif number == 'seven':
            result.append(7)
        elif number == 'eight':
            result.append(8)
        elif number == 'nine':
            result.append(9)
    return ' '.join([str(x) for x in sorted(result)])


'''
Standard answer: 
    value_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    return ' '.join(sorted([x for x in numbers.split(' ') if x], key=lambda x: value_map[x]))
'''


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == ''
    assert candidate('three') == 'three'
    assert candidate('three five nine') == 'three five nine'
    assert candidate('five zero four seven nine eight') == 'zero four five seven eight nine'
    assert candidate('six five four three two one zero') == 'zero one two three four five six'
check(sort_numbers)
