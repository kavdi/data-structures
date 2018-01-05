"""Implement insertion sort algorithm."""
from random import randint, shuffle
from timeit import timeit


def insertion_sort(arr):
    """Sort from lowest to highest with insertion method."""
    l = len(arr)
    for i in range(1, l):
        while i - 1 != -1:
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
            if i != 0:
                i = i - 1
    return arr


def timings():  # pragma: no cover
    """Generate timings report for insertion sort."""
    import_sort = 'from insertion import insertion_sort'
    print("""
    Timings for best, average and worst case scenarios for the insertion sort.
    --------------------------------------------------------------------------
    """)

    print("3 Best Case Scenarios - sorted except for one value")
    for i in range(3):
        lst_len = randint(9, 50)
        rand_lst = [i for i in range(lst_len)]
        rand_lst[6], rand_lst[-1] = rand_lst[-1], rand_lst[6]
        best_time = timeit('insertion_sort({})'.format(rand_lst), import_sort)
        print('List {}: length={}; time = {}'.format(i + 1, lst_len, best_time))

    print("\n3 Average Case Scenarios - Moderately sorted")
    for i in range(3):
        lst_len = randint(9, 50)
        rand_lst = [i for i in range(lst_len)]
        shuffle(rand_lst)
        best_time = timeit('insertion_sort({})'.format(rand_lst), import_sort)
        print('List {}: length={}; time = {}'.format(i + 1, lst_len, best_time))

    print("\n3 Worst Case Scenarios - Completely unsorted")
    for i in range(3):
        lst_len = randint(9, 50)
        rand_lst = [i for i in range(lst_len)]
        rand_lst = rand_lst[::-1]
        best_time = timeit('insertion_sort({})'.format(rand_lst), import_sort)
        print('List {}: length={}; time = {}'.format(i + 1, lst_len, best_time))


if __name__ == '__main__':  # pragma: no cover
    timings()
