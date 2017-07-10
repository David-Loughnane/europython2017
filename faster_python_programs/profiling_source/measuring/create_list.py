# file: create_list.py

import sys

if sys.version_info.major < 3:
    range = xrange


def insert_zero(n=int(1e4)):
    """Assemble list with `insert`. Inefficient.
    """
    L = []
    for x in range(n):
        L.insert(0, x)
    return L


def append_reverse(n=int(1e4)):
    """Assemble list with `append` and `reverse`.
    """
    L = []
    for x in range(n):
        L.append(x)
    L.reverse()
    return L
