
"""Test insertion sort module."""

from random import randint
import copy
import pytest
from insertion import insertion_sort


def random_list():
    """Generate a random list for testing."""
    bunch_of_lists = []
    for _ in range(100):
        lst_len = randint(1, 1000)
        rand_lst = [randint(1, 1000) for _ in range(lst_len)]
        copy_lst = copy.deepcopy(rand_lst)
        bunch_of_lists.append((rand_lst, sorted(copy_lst)))

    return bunch_of_lists

LISTS = random_list()


@pytest.mark.parametrize('to_sort, pre_sorted', LISTS)
def test_random_lists_always_sorted(to_sort, pre_sorted):
    """Test insertion sort works for 100 random lists."""
    assert insertion_sort(to_sort) == pre_sorted
