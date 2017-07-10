# file: pympler_list_growth.py

"""Measure the size of a list as it grows.
"""
from __future__ import print_function

import sys

from pympler.asizeof import asizeof, flatsize


if sys.version_info.major < 3:
    range = xrange


def list_mem(length, size_func=flatsize):
    """Measure incremental memory increase of a growing list.
    """
    my_list = []
    mem = [size_func(my_list)]
    for elem in range(length):
        my_list.append(elem)
        mem.append(size_func(my_list))
    return mem


if __name__ == '__main__':

    def main():
        """Show plot or numbers.
        """
        SIZE = 1000
        SHOW = 20

        for func in [flatsize, asizeof, sys.getsizeof]:
            mem = list_mem(SIZE, size_func=func)
            try:
                from matplotlib import pylab
                pylab.plot(mem)
                pylab.show()
            except ImportError:
                print('matplotlib seems not be installed. Skipping the plot.')
                if SIZE > SHOW:
                    limit = SHOW // 2
                    print(mem[:limit],
                          '... skipping %d elements ...' % (SIZE - SHOW),
                          end='')
                    print(mem[-limit:])
                else:
                    print(mem)
