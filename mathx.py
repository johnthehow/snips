import operator
from functools import reduce

def product(multipliers):
    return reduce(operator.mul, multipliers)