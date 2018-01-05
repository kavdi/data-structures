"""Implement merge sort algorithm."""


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
