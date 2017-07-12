import subprocess  # spawn new processes, contect their input/output/error pipes, and obtain their return codes
import time


def runner(argv, timeout=0):
    argv = [str(x) for x in argv]

    proc = subprocess.Popen(argv)
    t0 = time.time()

    while True:
        # polling - asking if its done
        returncode = proc.poll()
        if returncode is None:
            if timeout > 0 and time.time() - t0 >= timeout:
                proc.kill()
                raise subprocess.TimeoutExpired(cmd=' '.join(argv), timeout=timeout)
        else:
            return returncode
        # process is still running, and no timeout expired
        # not blocking, this is a generator function
        yield


if __name__ == "__main__":
    # a queue of coroutines
    coroutines = [
        runner(['sleep', 5], timeout=3),
        runner(['sleep', 5]),
        runner(['sleep', 5]),
        runner(['sleep', 5])
    ]

    while coroutines:
        coro = coroutines.pop(0)
        try:
            next(coro)
        except StopIteration as e:
            print(f'coroutine is done, result={e.value}')
        except Exception as e:
            print(f'coroutine raised {e}')
        else:
            coroutines.append(coro)
