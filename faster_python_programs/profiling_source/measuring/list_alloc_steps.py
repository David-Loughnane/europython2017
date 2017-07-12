# file: list_alloc_steps.py

"""Measure the number of memory allocation steps for a list.
"""
from __future__ import print_function

import sys

if sys.version_info.major < 3:
    range = xrange

from pympler.asizeof import flatsize


def list_steps(lenght, size_func=sys.getsizeof):
    """Measure the number of memory alloaction steps for a list.
    """
    my_list = []
    steps = 0
    int_size = size_func(int())
    old_size = size_func(my_list)
    for elem in range(lenght):
        my_list.append(elem)
        new_size = sys.getsizeof(my_list)
        if new_size - old_size > int_size:
            steps += 1
        old_size = new_size
    return steps


if __name__ == '__main__':
    steps = [10, 100, 1000, 10000, int(1e5), int(1e6), int(1e7)]
    print('Using sys.getsizeof:')
    for size in steps:
        print('%10d: %3d' % (size, list_steps(size)))
    print('Using pympler.asizeof.flatsize:')
    for size in steps:
        print('%10d: %3d' % (size, list_steps(size, flatsize)))
