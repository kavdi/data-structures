"""Tests for hash table module."""
import pytest


def test_additive_hash_raises_error_if_str_not_given():
    """Test that additive_hash raises type error if not given a string."""
    from hash import additive_hash
    with pytest.raises(TypeError):
        additive_hash(22)


@pytest.mark.parametrize('key, value', [('a', 97), ('b', 98), ('c', 99), ('d', 100), ('e', 101), ('hello', 532), ('bye', 320), ('start', 558), ('finish', 641)])
def test_additive_hash_returns_correct_values(key, value):
    """Test that additive hash returns the correct values."""
    from hash import additive_hash
    assert additive_hash(key) == value


def test_horner_hash_raises_error_when_key_not_string():
    """Test that TypeError raised if key given to horner hash is not string."""
    from hash import horner_hash
    with pytest.raises(TypeError):
        horner_hash(22)


@pytest.mark.parametrize('key, value', [('a', 97), ('b', 98), ('c', 99), ('d', 100), ('e', 101), ('hello', 99162322), ('bye', 98030), ('start', 109757538), ('finish', 3020524691)])
def test_horner_hash_returns_correct_hash_values_for_strings_given(key, value):
    """Test that horner hash returns correct values."""
    from hash import horner_hash
    assert horner_hash(key) == value


def test_hash_table_constructor_creates_empty_hash_table():
    """Test that HashTable constructor creates an empty hash table."""
    from hash import additive_hash, HashTable
    t = HashTable(10, additive_hash)
    assert len(t.buckets) == 10
    assert t.hash_func is additive_hash
    assert not all(t.buckets)


def test_hash_table_uses_additive_hash_function():
    """Test that hash table hashes keys with function provided."""
    from hash import additive_hash, HashTable
    t = HashTable(10, additive_hash)
    assert t._hash('one') == additive_hash('one')


def test_hash_table_uses_horner_hash_function():
    """Test that hash table hashes keys with function provided."""
    from hash import horner_hash, HashTable
    t = HashTable(10, horner_hash)
    assert t._hash('two') == horner_hash('two')


def test_set_raises_error_if_key_not_string():
    """Test that type error raised if key not string in set."""
    from hash import HashTable, additive_hash
    t = HashTable(10, additive_hash)
    with pytest.raises(TypeError):
        t.set(12, 44)


def test_set_places_key_value_pairs_in_hash_table():
    """Test that set function places key value pairs in hash table correctly."""
    from hash import HashTable, additive_hash
    t = HashTable(10, additive_hash)
    t.set('word', 444)
    assert t.buckets[4][0] == ['word', 444]


def test_get_returns_value_of_key_provided():
    """Test that get function returns the value of key provided."""
    from hash import HashTable, additive_hash
    t = HashTable(10, additive_hash)
    t.set('word', 444)
    assert t.get('word')


def test_get_raises_error_if_key_not_not_in_table():
    """Test that keyerror raised if key not in table."""
    from hash import HashTable, additive_hash
    t = HashTable(10, additive_hash)
    with pytest.raises(KeyError):
        t.get('key')


def test_get_non_string_key_raises_error():
    """Test taht get with a non string key raises error."""
    from hash import HashTable, additive_hash
    t = HashTable(10, additive_hash)
    with pytest.raises(TypeError):
        t.get(22)
