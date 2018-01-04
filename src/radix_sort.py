"""Implement radix sort algorithm."""


def radix_sort(arr):
    """Sort list of numberes with radix sort."""
    if len(arr) == 1:
        return arr
    buckets = [[] for _ in range(10)]
    
