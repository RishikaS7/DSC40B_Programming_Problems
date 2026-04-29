# Homework 4:  Programming Problem 1

import random

def knn_distance(arr, q, k):
    """    
    >>> knn_distance([3, 10, 52, 15], 19, 1)
    (4, 15)
    >>> knn_distance([3, 10, 52, 15,], 19, 2)
    (9, 10)
    >>> knn_distance([3, 10, 52, 15], 19, 3)
    (16, 3)
    """ 
    pairs = []
    for i in arr:
        pairs.append((abs(i - q), i))
    return quickselect(pairs, k, 0, len(pairs))

def quickselect(arr, k, start, stop):
    pivot_idx = random.randrange(start, stop)
    pivot_idx = partition(arr, start, stop, pivot_idx)
    pivot_order = pivot_idx + 1
    if pivot_order == k:
        return arr[pivot_idx]
    elif pivot_order < k:
        return quickselect(arr, k, pivot_idx + 1, stop)
    else:
        return quickselect(arr, k, start, pivot_idx)

def partition(arr, start, stop, pivot_ix):
    def swap(ix_1, ix_2):
        arr[ix_1], arr[ix_2] = arr[ix_2], arr[ix_1]

    pivot = arr[pivot_ix]
    swap(pivot_ix, stop-1)
    middle_barrier = start
    for end_barrier in range(start, stop - 1):
        if arr[end_barrier] < pivot:
            swap(middle_barrier, end_barrier)
            middle_barrier += 1
    swap(middle_barrier, stop-1)
    return middle_barrier