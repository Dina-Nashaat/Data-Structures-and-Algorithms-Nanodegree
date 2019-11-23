import math

def mergesort_descending(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = mergesort_descending(arr[:mid])
    right = mergesort_descending(arr[mid:])
    return merge(left, right)

def merge(left, right):
    left_index = 0
    right_index = 0
    merged = []

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
    return merged

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        return []

    digits = mergesort_descending(input_list)

    odd, even = 0, 0
    for i, val in enumerate(digits):
        if i % 2 == 0:
            odd =  odd * 10 + val
        else:
            even = even * 10 + val
    return [odd, even]

