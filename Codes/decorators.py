import time

def timed(callback):

    def wrapper(*args, **kwargs):
        start = time.time()
        value = callback(*args, **kwargs)
        end = time.time()
        print(f'Function {callback.__name__} took {end - start} seconds to execute..')
        return value

    return wrapper

@timed
def pow_of_five(x):
    res = 1
    for i in range(x):
        res *= 5

    return res

value = pow_of_five(200000)
