from collections import defaultdict
import subprocess  # spawn new processes, contect their input/output/error pipes, and obtain their return codes
import time


def sleep(n):
    yield n


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
        # yield from is delegating work to another generator
        # yield that value that is yielded from another generator
        yield from sleep(1)


class Task:
    # class property
    instances_created = 0

    def __init__(self, coroutine):
        self.coroutine = coroutine
        self.id = Task.instances_created
        Task.instances_created += 1

        self.callback = None

        self.result = None
        self.exception = None

    def add_done_callback(self, fn):
        self.callback = fn


class Loop:
    # synchronous code - you wait for results
    # async - throw code out there, react when it returns
    def __init__(self):
        self.tasks = []
        # everytime you put in a key it adds in a list
        self.ready_at = defaultdict(list)
        self.current_iteration = 0

    def create_task(self, coroutine):
        task = Task(coroutine)
        if self.current_iteration == 0:
            self.schedule(task, iteration=self.current_iteration)
        else:
            self.schedule(task, iteration=self.current_iteration + 1)
        return task

    def schedule(self, task, iteration=0):
        # don't want to schedule things in the past
        if iteration < self.current_iteration:
            iteration = self.current_iteration

        self.ready_at[iteration].append(task)
        if task not in self.tasks:
            self.tasks.append(task)

    def remove(self, task):
        self.tasks.remove(task)

    def run(self):
        # Event loop
        while self.tasks:
            for task in self.ready_at[self.current_iteration]:
                try:
                    # run after this many iterations (0 run at next iteration)
                    run_after = next(task.coroutine)
                except StopIteration as e:
                    task.result = e.value
                    if task.callback is not None:
                        task.callback(task)
                    self.remove(task)
                except Exception as e:
                    task.exception = e
                    if task.callback is not None:
                        task.callback(task)
                    self.remove(task)
                else:
                    run_next = (run_after * 100) + 1 + self.current_iteration
                    self.schedule(task, iteration=run_next)
            self.current_iteration += 1
            time.sleep(0.01)


def my_callback(task):
    if task.exception is not None:
        print(f'task {task.id} raised {task.exception}')
    else:
        print(f'task {task.id} done, result={task.result}')


if __name__ == "__main__":
    loop = Loop()
    loop.create_task(runner(['sleep', 10], timeout=5))
    loop.create_task(runner(['sleep', 10], timeout=0))
    loop.create_task(runner(['sleep', 10], timeout=0))
    loop.create_task(runner(['sleep', 10], timeout=0))
    loop.create_task(runner(['sleep', 10], timeout=0))

    for task in loop.tasks:
        task.add_done_callback(my_callback)

    loop.run()
