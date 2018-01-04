"""Implement quick sort algorithm."""


def quick_sort(arr):
    """Sort array of numbers with quicksort."""
    if len(arr) == 1:
        return arr
    if len(arr) > 1:
        pivot = arr[0]
        left = 1
        right = len(arr) - 1

        while left <= right:
            if arr[left] > pivot and arr[right] < pivot:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

            elif arr[left] <= pivot and arr[right] < pivot:
                left += 1

            elif arr[left] > pivot and arr[right] >= pivot:
                right -= 1

            elif arr[left] <= pivot and arr[right] >= pivot:
                left += 1
                right -= 1

        arr[0], arr[right] = arr[right], arr[0]

        divider = right + 1
        first = quick_sort(arr[:right])
        second = quick_sort(arr[divider:])
        return first + [arr[right]] + second
    else:
        return arr
