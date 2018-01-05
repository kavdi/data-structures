"""Implement merge sort algorithm."""
from random import randint, shuffle
from timeit import timeit


def merge_sort(nums):
    """Merge list by merge sort."""
    half = int(len(nums) // 2)
    if len(nums) == 1:
        return nums

    if len(nums) == 2:
        if nums[0] > nums[1]:
            nums[0], nums[1] = nums[1], nums[0]
        return nums

    left = merge_sort(nums[:half])
    right = merge_sort(nums[half:])

    output = []

    left_ct = 0
    right_ct = 0
    while left_ct < len(left) and right_ct < len(right):
        if left[left_ct] < right[right_ct]:
            output.append(left[left_ct])
            left_ct += 1
        else:
            output.append(right[right_ct])
            right_ct += 1

    if left_ct == len(left):
        output += right[right_ct:]
    elif right_ct == len(right):
        output += left[left_ct:]
    return output


def timings():  # pragma: no cover
    """Generate timings report for insertion sort."""
    import_sort = 'from merge_sort import merge_sort'
    print("""
    Timings for best, average and worst case scenarios for the merge sort.
    --------------------------------------------------------------------------
    """)

    print("3 Best Case Scenarios - sorted except for one value")
    for i in range(3):
        lst_len = randint(9, 50)
        rand_lst = [i for i in range(lst_len)]
        rand_lst[6], rand_lst[-1] = rand_lst[-1], rand_lst[6]
        best_time = timeit('merge_sort({})'.format(rand_lst), import_sort)
        print('List {}: length={}; time = {}'.format(i + 1, lst_len, best_time))

    print("\n3 Average Case Scenarios - Moderately sorted")
    for i in range(3):
        lst_len = randint(9, 50)
        rand_lst = [i for i in range(lst_len)]
        shuffle(rand_lst)
        best_time = timeit('merge_sort({})'.format(rand_lst), import_sort)
        print('List {}: length={}; time = {}'.format(i + 1, lst_len, best_time))

    print("\n3 Worst Case Scenarios - Completely unsorted")
    for i in range(3):
        lst_len = randint(9, 50)
        rand_lst = [i for i in range(lst_len)]
        rand_lst = rand_lst[::-1]
        best_time = timeit('merge_sort({})'.format(rand_lst), import_sort)
        print('List {}: length={}; time = {}'.format(i + 1, lst_len, best_time))


if __name__ == '__main__':  # pragma: no cover
    timings()
