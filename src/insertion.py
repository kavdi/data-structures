"""Implement insertion sort algorithm."""


def insertion_sort(arr):
    """Sort from lowest to highest with insertion method."""
    l = len(arr)
    import pdb; pdb.set_trace()
    for i in range(1, l):
        x = i
        while x > 0:
            if arr[x] < arr[x - 1]:
                arr[x - 1], arr[x] = arr[x], arr[x - 1]
                x = x - 1
    return arr
