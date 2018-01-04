"""Implement quick sort algorithm."""


def quick_sort(arr):
    """Sort array of numbers with quicksort."""
    if len(arr) == 1:
        return arr
    if len(arr) > 1:
        pivot = arr[0]
        left = 1
        right = len(arr) - 1
