"""Implement a Hash table for storing strings."""


def additive_hash(key):
    """Hash string by adding up the values of the characters."""
    if not isinstance(key, str):
        raise TypeError("Key must be a string.")
    hv = sum(ord(letter) for letter in key)
    return hv


def horner_hash(key):
    """Hash key using horner's hashing algorithm."""
    if not isinstance(key, str):
        raise TypeError("Key must be a string.")
    hv = 0
    for letter in key:
        hv = 31 * hv + ord(letter)
    return hv


class HashTable(object):
    """Implement hash table class object for hashing strings."""

    def __init__(self, size, hash_func):
        """Initialize empty hash table with size and function used for hashing."""
        self.buckets = [[] for _ in range(size)]
        self.hash_func = hash_func

    def _hash(self, key):
        """Get hash value of key provided."""
        return self.hash_func(key)

    def set(self, key, value):
        """Set key value pair in hash table."""
        try:
            place = self._hash(key) % len(self.buckets)
        except TypeError:
            raise TypeError("Key must be a string.")

        if self.buckets[place]:
            for bucket in self.buckets[place]:
                if bucket[0] == key:
                    bucket[1] = value
                    return

        self.buckets[place].append([key, value])

    def get(self, key):
        """Return value stored with given key."""
        try:
            place = self._hash(key) % len(self.buckets)
        except TypeError:
            raise TypeError("Key must be a string.")

        for bucket in self.buckets[place]:
            if bucket[0] == key:
                return bucket[1]

        raise KeyError("Key does not exist in table.")
