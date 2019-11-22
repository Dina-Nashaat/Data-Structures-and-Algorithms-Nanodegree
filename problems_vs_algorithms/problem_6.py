def compare(x, y):
    """
    Return a tuple(min, max).
    """
    if x > y:
        return y, x
    else:
        return x, y

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
    ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None
    if len(ints) == 1:
        return ints[0], ints[0]
    
    start = 0
    if len(ints) % 2 == 0:
        globalMin, globalMax = compare(ints[start], ints[start+1])
        start += 2
    else:
        globalMin, globalMax = ints[start], ints[start]
        start += 1
    for i in range(start, len(ints), 2):
        localMin, localMax = compare(ints[i], ints[i+1])
        _, globalMax = compare(globalMax, localMax)
        globalMin, _  = compare(globalMin, localMin) 
    return globalMin, globalMax
