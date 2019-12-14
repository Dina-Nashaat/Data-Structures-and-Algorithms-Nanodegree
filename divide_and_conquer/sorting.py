
# arr = [p...r]
# GROUP L (less than pivot) : [p ... q-1]
# GROUP G (greater than pivot): [q ... j - 1]
# GROUP U (unknown): [ j ... r - 1]
# GROUP P (pivot): [r]
def partition(arr, p, r):
    q, j = p, p
    pivot = 0
    while j < r:
        if arr[j] > pivot:
            j += 1
        else:
            arr[j], arr[q] = arr[q], arr[j]
            j += 1
            q += 1
    arr[r], arr[q] = arr[q], arr[r]
    return q

def _quicksort(arr, start, end):
    if start > end:
        return    
    pivot_index = partition(arr, start, end)
    _quicksort(arr, start, pivot_index - 1)
    _quicksort(arr, pivot_index + 1, end)
    
def quicksort(arr):
    return _quicksort(arr, 0, len(arr) - 1)


def mergesort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
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


# arr1 = [8, 3, 1, 7, 0, 10, 2, 1]
# quicksort(arr1)
# print('quicksort', arr1)
# arr2 = [8, 3, 1, 7, 0, 10, 2, 1]
# print('mergesort', mergesort(arr2))

def partition0(arr, p, r):
    q, j = p, p
    pivot = 0
    while j < r:
        if arr[j] <= pivot:
            j += 1
        else:
            arr[j], arr[q] = arr[q], arr[j]
            j += 1
            q += 1
    arr[r], arr[q] = arr[q], arr[r]
    return q
arr = [1, 2, 6,0, 3, 9, 0, 2, 1]
partition0(arr, 0, len(arr) - 1)
print(arr)