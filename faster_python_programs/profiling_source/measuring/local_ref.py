# local_ref.py

"""Testing access to local name and name referenced in another module.
"""

import math
import sys

if sys.version_info.major < 3:
    range = xrange

# If there is no decorator `profile`, make one that just calls the function,
# i.e. does nothing.
# This allows to call `kernprof` with and without the option `-l` without
# commenting or un-commentimg `@profile' all the time.
# You can add this to the builtins to make it available in the whole program.
try:
    @profile
    def dummy():
        """Needs to be here to avoid a syntax error.
        """
        pass
except NameError:
    def profile(func):
        """Will act as the decorator `profile` if it was already found.
        """
        return func

@profile
def local_ref(counter):
    """Access local name.
    """
    # make it local
    sqrt = math.sqrt
    for _ in range(counter):
        sqrt

@profile
def module_ref(counter):
    """Access name as attribute of another module.
    """
    for _ in range(counter):
        math.sqrt


@profile
def test(counter):
    """Call both functions.
    """
    local_ref(counter)
    module_ref(counter)

if __name__ == '__main__':
    test(int(1e7))
