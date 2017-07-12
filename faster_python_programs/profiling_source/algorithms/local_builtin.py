"""Local vs. built-in.
"""

import sys

if sys.version_info.major < 3:
    range = xrange


def repeat(counter):
    """Using the built-in `sum` in a loop.
    """
    for count in range(counter):
        sum


def repeat_local(counter):
    """Making `sum` a local variable.
    """
    sum_ = sum
    for count in range(counter):
        sum_


def test(counter):
    """Call both functions.
    """
    repeat(counter)
    repeat_local(counter)


if __name__ == '__main__':

    def do_profile():
        """Check the run times.
        """
        import cProfile
        profiler = cProfile.Profile()
        profiler.run('test(int(1e8))')
        profiler.print_stats()

    do_profile()
