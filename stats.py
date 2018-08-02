
import numpy as np
import math

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
    unique_values = set(values)
    dic = {}
    for elem in unique_values:
        dic[elem] = values.count(elem)

    modals = []
    max = 0

    for k,v in dic.items():
        if v > max:
            modals = [k]
            max = v
        elif v == max:
            modals.append(k)
    
    if len(modals) == len(unique_values):
        modals = []
    return modals, max

def variance(values):
    """Assume degree of freedom = 0"""
    m = mean(values)
    n = len(values)
    mean_deviation_list = [(x - m)**2 for x in values]
    return sum(mean_deviation_list) / n 

def standard_deviation(values):
    """Assume degree of freedom = 0"""
    v = variance(values)
    return math.sqrt(v)

