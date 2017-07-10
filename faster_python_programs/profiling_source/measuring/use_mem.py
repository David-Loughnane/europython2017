# file: use_mem.py

import random
import sys

# Make it work with Python 2 and Python 3.
if sys.version_info.major < 3:
    range = xrange


@profile
def use_mem(numbers):
    """Different ways to use up memory.
    """
    a = sum([x * x for x in numbers])
    b = sum(x * x for x in numbers)
    c = sum(x * x for x in numbers)
    squares = [x * x for x in numbers]
    d = sum(squares)
    del squares
    x = 'a' * int(1e6)
    del x
    return 42


if __name__ == '__main__':

    numbers = [random.random() for x in range(int(1e6))]
    use_mem(numbers)