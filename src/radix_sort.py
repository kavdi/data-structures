"""Implement radix sort algorithm."""


def radix_sort(arr):
    """Sort list of numberes with radix sort."""
    if len(arr) > 1:
        buckets = [[] for x in range(10)]
        lst = arr
        output = []
        t = 0
        m = len(str(max(arr)))
        while m > t:
            for num in lst:
                if len(str(num)) >= t + 1:
                    for b_num in range(10):
                        idx = num // 10**t % 10
                        if idx == b_num:
                            buckets[b_num].append(num)
                            break
                else:
                    output.append(num)
            lst = []
            for bucket in buckets:
                lst += bucket
            buckets = [[] for x in range(10)]
            t += 1
        output += lst
        return output
    else:
        return arr
