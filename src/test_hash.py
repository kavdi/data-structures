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


def test_Hahs_Table_uses_provided_hash_function():
    """Test that hash table hashes keys with function provided."""
    