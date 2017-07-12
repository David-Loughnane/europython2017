"""
Simple example of a generator function in pure Python.
"""


def myrange(n):
    # returns a generator object
    # the aggreagation of code and state

    # this code won't be executed until we first call next
    # not on instantiation of function
    # eg >> x = myrange(-1). won't raise exception
    assert n >= 0

    i = 0
    while i < n:
        # fundamental mechanism for generators
        # generators can inject values at the yield points
        yield i
        # code is not running past this (hibernating)
        # if called again, resumes running from here
        i += 1
    # if the function exits without hitting yield, it will raise StopIteration exception


if __name__ == '__main__':
    # for x in myrange(10):
    #     print(x)
    #
    # print(list(myrange(10)))

    # coro = myrange(10)
    # print(coro)
    # print(coro.send(None))
    # print(next(coro))
    # print(coro.send(None))
    # print(coro.send(None))
    # print(coro.send(None))
    # print(coro.send(None))
    # print(coro.send(None))
    # print(coro.send(None))
    # print(coro.send(None))
    # print(coro.send(None))
    # print(coro.send(None))

    coro = myrange(10)
    coro.send(None)

    while True:
        try:
            print(coro.send(None))
        except StopIteration:
            break
