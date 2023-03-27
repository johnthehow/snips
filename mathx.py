import operator
from functools import reduce

def product(numbers):
    return reduce(operator.mul, numbers)