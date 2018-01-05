"""Test the Trie."""
from trie import Trie
from faker import Faker
import pytest


FAKE = Faker()


def test_trie_initiates_with_root_node(empty_trie):
    """Instantiate tree should have a root node."""
    assert empty_trie.root


def test_trie_root_node_value_is_star(empty_trie):
    """Instantiating trie should create node with a value '*'."""
    assert empty_trie.root.value == '*'


def test_trie_root_node_childen_is_empty_dict(empty_trie):
    """Instatiating trie should create root with children attribute as dict."""
    assert empty_trie.root.children == {}


def test_trie_root_node_end_is_false(empty_trie):
    """Instantiate trie, root 'end' attribute should be false."""
    assert not empty_trie.root.end


def test_trie_instatiates_with_size_zero(empty_trie):
    """Instantiate trie should have size of zero."""
    assert empty_trie._size == 0


def test_non_iter_passed_to_trie_raises_error():
    """Trie instantiated with string as iter raises Value."""
    with pytest.raises(TypeError):
        Trie('word')


def test_valid_iter_passed_increases_trie_size(trie_3):
    """Trie instantiated with valid iter should increase size."""
    assert trie_3._size == 3


def test_insert_not_string_raises_error(empty_trie):
    """A non string passed to insert should raise type error."""
    with pytest.raises(TypeError):
        empty_trie.insert(1)


def test_insert_string_trie_size_increases_correctly(empty_trie):
    """Trie size should increase by 1 for every word inserted."""
    for i in range(1, 51):
        empty_trie.insert(FAKE.word())
        assert empty_trie._size == i


def test_contains_raises_error(empty_trie):
    """Contain method should raise type error if passed non string."""
    with pytest.raises(TypeError):
        empty_trie.contains(1)


def test_contains_finds_only_word(empty_trie):
    """Search should find word if only word in trie."""
    empty_trie.insert('spectacular')
    assert empty_trie.contains('spectacular')


def test_contains_doesnt_find_only_word(empty_trie):
    """Contain shouldn't find word not in trie."""
    empty_trie.insert('bonanza')
    assert not empty_trie.contains('absent')


def test_contains_doesnt_find_only_word_if_similar(empty_trie):
    """Contain shouldn't find word not in trie."""
    empty_trie.insert('bonanza')
    assert not empty_trie.contains('bonanze')


def test_contains_finds_one_of_3_similar_words(trie_3):
    """Trie with 3 similar words finds all 3 words."""
    words = ['potato', 'potatoes', 'pot']
    for word in words:
        assert trie_3.contains(word)


def test_contains_finds_word_one_letter_different(empty_trie):
    """If word is one letter less than another in trie and not in trie, it
    should not be found."""
    empty_trie.insert('apples')
    assert not empty_trie.contains('apple')


def test_partial_match_returns_false(trie_3):
    """If word is partial match of another word, contains returns false."""
    assert not trie_3.contains('pots')


def test_size_method_returns_actual_size(empty_trie):
    """Trie size should increase by 1 for every word inserted."""
    for i in range(1, 51):
        empty_trie.insert(FAKE.word())
        assert empty_trie.size() == i
        

def test_remove_not_string_raises_error(trie_3):
    """A non string passed to remove should raise type error."""
    with pytest.raises(TypeError):
        trie_3.remove(1)


def test_remove_error_if_no_string(trie_3):
    """If word not in trie, remove raises Value Error."""
    with pytest.raises(ValueError):
        trie_3.remove('banana')


def test_remove_word_removes_word(trie_3):
    """If word in trie remove should remove it."""
    trie_3.remove('potato')
    with pytest.raises(ValueError):
        trie_3.remove('potato')


def test_remove_word_that_doesnt_share_root_node_with_another(empty_trie):
    """If 2 words in trie and they don't start with same letter."""
    empty_trie.insert('broom')
    empty_trie.insert('bananas')
    assert not empty_trie.remove('bananas')
