from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()

        print('func:%r args:[%r, %r] took: %2.4f sec' %
              (f.__name__, args, kw, te-ts))

        return result
    return wrap


@timing
def bottleneck(limit):
    return [i ** i for i in range(limit)]


res = [bottleneck(x) for x in [10, 1000, 10000]]
