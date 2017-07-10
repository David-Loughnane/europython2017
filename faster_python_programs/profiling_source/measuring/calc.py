#calc.py

"""Simple test function for line_profiler doing some math.
"""

import math
import sys

if sys.version_info.major < 3:
    range = xrange


@profile
def calc(number, loops=1000):
    """Do some math calculations.
    """
    sqrt = math.sqrt
    for x in range(loops):
        x = number + 10
        x = number * 10
        x = number ** 10
        x = pow(number, 10)
        x = math.sqrt(number)
        x = sqrt(number)
        math.sqrt
        sqrt

if __name__ == '__main__':
    calc(100, int(1e5))
