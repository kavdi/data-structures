"""Implement quick sort algorithm."""
from random import randint, shuffle
from timeit import timeit


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


def timings():  # pragma: no cover
    """Generate timings report for insertion sort."""
    import_sort = 'from quick import quick_sort'
    print("""
    Timings for best, average and worst case scenarios for the merge sort.
    --------------------------------------------------------------------------
    """)

    print("3 Best Case Scenarios - sorted except for one value")
    for i in range(3):
        lst_len = randint(9, 50)
        rand_lst = [i for i in range(lst_len)]
        rand_lst[6], rand_lst[-1] = rand_lst[-1], rand_lst[6]
        best_time = timeit('quick_sort({})'.format(rand_lst), import_sort)
        print('List {}: length={}; time = {}'.format(i + 1, lst_len, best_time))

    print("\n3 Average Case Scenarios - Moderately sorted")
    for i in range(3):
        lst_len = randint(9, 50)
        rand_lst = [i for i in range(lst_len)]
        shuffle(rand_lst)
        best_time = timeit('quick_sort({})'.format(rand_lst), import_sort)
        print('List {}: length={}; time = {}'.format(i + 1, lst_len, best_time))

    print("\n3 Worst Case Scenarios - Completely unsorted")
    for i in range(3):
        lst_len = randint(9, 50)
        rand_lst = [i for i in range(lst_len)]
        rand_lst = rand_lst[::-1]
        best_time = timeit('quick_sort({})'.format(rand_lst), import_sort)
        print('List {}: length={}; time = {}'.format(i + 1, lst_len, best_time))


if __name__ == '__main__':  # pragma: no cover
    timings()
