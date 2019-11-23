def sort_012_method_1(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    pivot, start, mid, end = 1, 0, 0, len(input_list) - 1
    while mid <= end:
        if input_list[mid] < pivot:
            swap(input_list, start, mid)
            start, mid = start + 1, mid + 1
        elif input_list[mid] > pivot:
            swap(input_list, end, mid)
            end -= 1
        else:
            mid += 1
    return input_list

def sort_012_method_2(input_list):
    mid = partition(input_list, 0, len(input_list) - 1, 1)
    partition(input_list, 0, mid, 0.5)
    return input_list

def partition(arr, p, r, pivot):
    q, j = p, p
    while j < r:
        if arr[j] > pivot:
            j += 1
        else:
            swap(arr, j, q)
            j, q = j + 1, q + 1
    arr[r], arr[q] = arr[q], arr[r]
    return q

def swap(input_list, start, end):
    input_list[start], input_list[end] = input_list[end], input_list[start]

def test_function(test_case):
    sorted_array = sort_012_method_1(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")
