# file: simple_pi.py

"""Calculating pi with Monte Carlo.
"""

from __future__ import print_function

import math
import random
import sys


if sys.version_info[0] < 3:
    range = xrange


def pi_plain(total):
    """Calculate pi with `total` hits.
    """
    count_inside = 0
    for _ in range(total):
        x = random.random()
        y = random.random()
        dist = math.sqrt(x * x + y * y)
        if dist < 1:
            count_inside += 1
    return 4.0 * count_inside / total

if __name__ == '__main__':

    def test():
        """Check if it works.
        """
        n = int(1e6)
        print('pi:', pi_plain(n))

    test()
