# file: measuring/clock_check.py

"""Checking different timing functions.
"""

from __future__ import print_function

import os
import sys
import time
import timeit


if sys.version_info.major < 3:
    range = xrange


def clock_check(duration=1):
    """Check the measured time with different methods.
    """
    start_os_time0 = os.times()[0]
    start_time_clock = time.clock()
    start_default_timer = timeit.default_timer()
    for _ in range(int(1e6)):
        1 + 1
    time.sleep(duration)
    durtation_os_time0 = os.times()[0] - start_os_time0
    durtation_time_clock = time.clock() - start_time_clock
    durtation_default_timer = timeit.default_timer() - start_default_timer
    print('durtation_os_time0:     ', durtation_os_time0)
    print('durtation_time_clock:   ', durtation_time_clock)
    print('durtation_default_timer:', durtation_default_timer)


if __name__ == '__main__':
    clock_check()
