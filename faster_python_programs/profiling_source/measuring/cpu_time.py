# file: cpu_time.py

"""Measuring CPU time instead of wall clock time.
"""

import cProfile
import os
import sys
import time

# Make it work with Python 2 and Python 3.
if sys.version_info.major < 3:
    range = xrange


def cpu_time():
    """Function for cpu time. Os dependent.
    """
    if sys.platform == 'win32':
        return os.times()[0]
    else:
        return time.clock()


def sleep():
    """Wait 2 seconds.
    """
    time.sleep(2)


def count():
    """100 million loops.
    """
    for _ in range(int(1e8)):
        1 + 1


def test():
    """Run functions
    """
    sleep()
    count()


def profile():
    """Profile with wall clock and cpu time.
    """
    profiler = cProfile.Profile()
    profiler.run('test()')
    profiler.print_stats()

    profiler = cProfile.Profile(cpu_time)
    profiler.run('test()')
    profiler.print_stats()

if __name__ == '__main__':
    profile()
