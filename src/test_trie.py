"""Test trie module."""


def test_node_object_has_correct_value_attributes():
    """Test that new node has correct value."""
    from trie import Node
    n = Node('t')
    assert n.value == 't'
    assert n.end is False
    assert n.children == {}


def test_empty_trie_tree_has_all_attributes():
    """Test empty trie has correct attributes."""
    from trie import Trie
    t = Trie()
    assert t.root
    assert t.root.value == '*'
    assert t._size == 0
