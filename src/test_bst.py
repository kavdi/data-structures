"""Test binary search tree module."""

import pytest


def test_node_object_has_value_and_left_right_are_none():
    """Test node constructure creates node with left and right children."""
    from bst import Node
    n = Node(5)
    assert n.value == 5
    assert n.left is None
    assert n.right is None


def test_node_has_value_and_left_right_have_value_when_given():
    """Test node node has value given and contains value for left and right."""
    from bst import Node
    n = Node(4, 3, 5)
    assert n.value == 4
    assert n.left == 3
    assert n.right == 5


def test_bst_object_root_is_none():
    """Test initiation of bst object has a root of None."""
    from bst import BST
    t = BST()
    assert t.root is None


def test_bst_takes_an_iterable_and_firts_value_is_root():
    """Test bst takes in an iterable and the first value is the root."""
    from bst import BST
    t = BST([8])
    assert t.root.value == 8


def test_bst_root_has_value_and_left_and_right_are_none_if_not_given():
    """Test that root has value and left, right value are none."""
    from bst import BST
    t = BST([4])
    assert t.root.value == 4
    assert t.root.right is None
    assert t.root.left is None


def test_bst_root_has_left_and_right_value_if_given():
    """Test that root, left and right have values when given."""
    from bst import BST
    t = BST([8, 5, 9])
    assert t.root.value == 8
    assert t.root.right.value == 9
    assert t.root.left.value == 5


def test_bst_takes_iterable_and_creates_bst(filled_bst):
    """Test that bst takes in an itterable ."""
    assert filled_bst.root.value == 13


def test_insert_value_into_emtpy_bst_creates_root_node_with_value_inerted():
    """Test that inserting value into empty bst creates root node."""
    from bst import BST
    t = BST()
    t.insert(5)
    assert t.root
    assert t.root.value == 5


def test_insert_value_already_in_bst_raises_value_error(filled_bst):
    """Test that a value error is raised when inserting a value already in tree."""
    with pytest.raises(ValueError):
        filled_bst.insert(13)


def test_insert_value_less_than_root_value_creates_left_node_child():
    """Test inserting value less than root value creates left child node of root."""
    from bst import BST
    t = BST([5])
    t.insert(4)
    assert t.root.left.value == 4
    assert t.root.right is None


def test_insert_value_grater_than_root_creates_right_node_child():
    """Test inserting value grater than root value creates right childe node of root."""
    from bst import BST
    t = BST([5])
    t.insert(7)
    assert t.root.right.value == 7
    assert t.root.left is None


def test_search_of_value_not_in_bst_is_none():
    """Test searching for value not in bst returns none."""
    from bst import BST
    t = BST()
    assert t.search(5) is None


def test_search_for_value_in_bst_returns_node_with_correct_value():
    """Test that searching for value of node in tree returns correct node with value."""
    from bst import BST
    t = BST([1])
    t.search(1)
    assert t.root.value == 1


@pytest.mark.parametrize('val', [x for x in range(20)])
def test_search_for_value_in_bst_returns_correct_value(val):
    """Test search for value in bst returns node with correct value."""
    from bst import BST
    t = BST()
    t.insert(val)
    assert t.search(val).value == val


def test_search_for_value_in_full_bst_returns_node_with_value_and_child_nodes(filled_bst):
    """Test search for node in filled bst returns node and child nodes with correct values."""
    t = filled_bst
    assert t.search(13).value == 13
    assert t.search(13).left.value == 10
    assert t.search(13).right.value == 15


def test_size_is_zero_in_empty_bst():
    """Test that size is zero when there are no nodes in bst."""
    from bst import BST
    t = BST()
    assert t.size() == 0


def test_size_is_one_when_only_one_node_added_to_empty_bst():
    """Test when adding one node to empty bst size is one."""
    from bst import BST
    t = BST()
    t.insert(1)
    assert t.size() == 1


def test_size_goes_up_with_each_value_inserted_to_bst():
    """Test that size increases by one with every value inserted."""
    from bst import BST
    t = BST()
    t.insert(4)
    t.insert(3)
    t.insert(5)
    t.insert(7)
    assert t.size() == 4


def test_depth_returns_0_when_bst_is_empty():
    """Test that empty bst returns none when checked for depth."""
    from bst import BST
    t = BST()
    assert t.depth() == 0 


def test_depth_returns_0_when_one_node_in_bst():
    """Test that depth returns 0 when only one node in bst."""
    from bst import BST
    t = BST([1])
    assert t.depth() == 0


def test_depth_returns_1_when_at_most_two_nodes_in_bst():
    """Test that depth returns one when two nodes in bst."""
    from bst import BST
    t = BST([4, 3])
    assert t.depth() == 1


def test_depth_gets_correct_depth_of_tree(filled_bst):
    """Test that depth returns correct depth of tree when nodes are added."""
    t = filled_bst
    assert t.depth() == 7


def test_contains_returns_false_when_bst_empty():
    """Test empty bst returns false when contains with value is initiated."""
    from bst import BST
    t = BST()
    assert t.contains(0) is False


@pytest.mark.parametrize('val', [x for x in range(0, 20)])
def test_contains_returns_false_if_value_not_in_bst(val):
    """Test contains returns false if value is not in the tree."""
    from bst import BST
    t = BST()
    t.insert(3)
    t.insert(1)
    t.insert(5)
    assert t.contains(23) is False


@pytest.mark.parametrize('val', [x for x in range(0, 20)])
def test_contains_returns_true_if_value_in_bst(val):
    """Test contains returns true if value in bst."""
    from bst import BST
    t = BST()
    t.insert(val)
    assert t.contains(val) is True


def test_balance_returns_string_if_bst_is_empty():
    """Test that balance returns 'tree is empty' if bst is empty."""
    from bst import BST
    t = BST()
    assert t.balance() == 'Tree is empty.'


def test_balane_returns_negative_number_if_left_branch_is_lower():
    """Test that balance returns a negative number when left side of tree is higher."""
    from bst import BST
    t = BST([9, 8, 7, 4, 6, 5, 1, 10, 14, 11])
    assert t.balance() == -2


def test_balance_returns_positive_number_if_right_branch_is_lower():
    """Test that balance returns a positive number when right side is higher."""
    from bst import BST
    t = BST([9, 8, 5, 14, 25, 15, 29])
    assert t.balance() == 1
