# file profile_me_use_line_profiler.py

"""Example to be profiled.
"""

import time
import sys

if sys.version_info.major < 3:
    range = xrange


def fast():
    """Wait 0.001 seconds.
    """
    time.sleep(1e-3)


def slow():
    """Wait 0.1 seconds.
    """
    time.sleep(0.1)

@profile
def use_fast():
    """Call `fast` 100 times.
    """
    for _ in range(100):
        fast()

@profile
def use_slow():
    """Call `slow` 100 times.
    """
    for _ in range(100):
        slow()


if __name__ == '__main__':
    use_fast()
    use_slow()
