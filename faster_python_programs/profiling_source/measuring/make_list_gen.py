#file: make_list_gen.py

from __future__ import print_function

import sys
import time

if sys.version_info.major < 3:
    range = xrange


def make_list(n):
    return [x * 10 for x in range(n)]


def make_gen(n):
    return (x * 10 for x in range(n))


def test():
    n = int(1e4)  # 1e5, 1e6, 1e7, 1e8
    list_ = make_list(n)
    del list_
    gen = make_gen(n)
    del gen
    time.sleep(1)

test()
