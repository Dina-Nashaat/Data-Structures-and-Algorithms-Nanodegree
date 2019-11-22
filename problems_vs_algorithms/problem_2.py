def search_rotated(input_list, target):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return _search_rotated(input_list, 0, len(input_list) - 1, target)

def _search_rotated(input_list, start, end, target):
    if start > end:
        return -1

    mid = ((end - start) // 2) + start
    mid_element = input_list[mid]

    if target == mid_element:
        return mid
    else:
        if input_list[mid] >= input_list[start]: # first half is sorted
            if target <= input_list[mid] and target >= input_list[start]: # target in first sorted half
                return _search_rotated(input_list, start, mid - 1, target)
            else:
                return _search_rotated(input_list, mid + 1, end, target)

        elif input_list[end] >= input_list[mid]: # second half is sorted
            if target <= input_list[end] and target >= input_list[mid]:
                return _search_rotated(input_list, mid + 1, end, target) # target in second sorted half
            else:
                return _search_rotated(input_list, start, mid - 1, target)
        else:
            return -1   


