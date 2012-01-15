import random

# returns a random number in positive integer range [p, r]
def Random(p, r):
    return int(p + round(random.random()*(r-p)))

def random_permutation(iterable, r=None):
    "Random selection from itertools.permutations(iterable, r)"
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(random.sample(pool, r))


