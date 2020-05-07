import math
import random

def slowfun(x, y, cache={}):
    # TODO: Modify to produce the same results, but much faster
    if ('pow', x, y) not in cache:
        cache[('pow', x, y)] = math.pow(x, y)
    v = cache[('pow', x, y)]

    if ('fac', x, y) not in cache:
        cache[('fac', v)] = math.factorial(v)
    v = cache[('fac', v)]

    v //= (x + y)

    v %= 982451653

    return v

# If we build a look-up table for each calculation
# We can store keys as either single values or tuples


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
