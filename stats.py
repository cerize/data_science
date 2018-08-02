
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

def covariance(A, B):
    """Assume A and B are the same length"""
    n = len(A)
    mean_of_A = mean(A)
    mean_of_B = mean(B)
    mean_deviation_A = [(x - mean_of_A) for x in A]
    mean_deviation_B = [(x - mean_of_B) for x in B]
    deviation_multiplication = [x * y for x, y in zip(mean_deviation_A, mean_deviation_B)]
    cov  = sum(deviation_multiplication) / n
    return cov

def correlation(A, B):
    """
    Assume A and B are the same length
    Assume non-corrected std
    """
    std_A = standard_deviation(A)
    std_B = standard_deviation(B)
    cov_A_B = covariance(A, B)
    corr = cov_A_B / (std_A * std_B)
    print('corr ddd', corr)
    return corr

