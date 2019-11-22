def sqrt_recursive(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        raise ValueError('Value must be greater than 0')
    return _sqrt_recursive(0, number, number)

def _sqrt_recursive(low, high, number):
    if  low > high:
        return high
    _root = (low + high) // 2
    if _root * _root == number:
        return _root
    elif _root * _root > number:
        return _sqrt_recursive(low, _root - 1, number)
    else:
        return _sqrt_recursive(_root + 1, high, number)
