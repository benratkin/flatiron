import math


def mean_normalize(data):
    mean = sum(data) / len(data)
    normalized_mean = [x - mean for x in data]
    return normalized_mean

def dot_product(x, y):
    return sum([tup[0]*tup[1] for tup in zip(x, y)])

def covariance(var1, var2):
    return dot_product(mean_normalize(var1), mean_normalize(var2)) / (len(var1) -1)

def correlation(var1, var2):
    var1_norm_mean = mean_normalize(var1)
    var2_norm_mean = mean_normalize(var2)
    var1_denom = sum([x**2 for x in var1_norm_mean])
    var2_denom = sum([y**2 for y in var2_norm_mean])
    return dot_product(var1_norm_mean, var2_norm_mean) / math.sqrt(var1_denom * var2_denom)

