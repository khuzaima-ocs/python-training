from contextlib import contextmanager
from time import time, sleep

@contextmanager
def timed(cb):
    start = time()
    yield cb
    end = time()
    print(f"Function took {end - start} seconds to execute..")


def foo():
    sleep(2)

with timed(foo) as f:
    f()
