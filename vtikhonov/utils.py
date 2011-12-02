import random

# returns a random number in positive integer range [p, r]
def Random(p, r):
    return int(p + round(random.random()*(r-p)))

