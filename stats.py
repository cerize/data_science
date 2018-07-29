
import numpy as np

def mean(values):
    try:
        n = len(values)
        return sum(values) / n
    except ZeroDivisionError:
        raise Exception('Cannot calculate mean of an empty list')


def median(values):
    n = len(values) 
    values.sort()
  
    if n % 2 == 0:
        upper_middle = values[int(n/2)]
        lower_middle = values[int(n/2) - 1]
        return mean([upper_middle, lower_middle])

    middle_value = values[int(n/2)]
    return middle_value

def mode(values):
    return 'todo'

def variance(values):
    return 'todo'

def standard_variation(values):
    return 'todo'

