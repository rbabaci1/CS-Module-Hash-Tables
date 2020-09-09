import random, math
from time import time

# Your code here


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= x + y
    v %= 982451653

    return v


table = {}


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    if f"{x}_{y}" not in table:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= x + y
        v %= 982451653
        table[f"{x}_{y}"] = v

    return table[f"{x}_{y}"]


# Do not modify below this line!
start = time()

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f"{i}: {x},{y}: {slowfun(x, y)}")

print(f"It took {time() - start} seconds.")
