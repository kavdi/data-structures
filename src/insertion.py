"""Implement insertion sort algorithm."""


def insertion_sort(arr):
    """Sort from lowest to highest with insertion method."""
    l = len(arr)
    # import pdb; pdb.set_trace()
    for i in range(1, l):
        while i - 1 != -1:
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
            if i != 0:
                i = i - 1
    return arr
