import operator
from functools import reduce

def product(multipliers): # 20230330152948
    return reduce(operator.mul, multipliers)