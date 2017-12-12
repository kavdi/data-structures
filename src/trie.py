"""Implement a trie tree."""


class Node(object):
    """Instance of node object."""

    def __init__(self, value):
        """Initiate Node instance."""
        self.value = value
        self.children = {}
        self.parent = None
        self.end = False


class Trie(object):
    """Instance of trie tree."""

    def __init__(self, itr=None):
        """Initiate Trie tree."""
        self.root = Node('*')
        self._size = 0
        if itr:
            if not isinstance(itr, (list, tuple, set)):
                raise TypeError('Must use itterable of strings.')
            else:
                for word in itr:
                    self.insert(word)

    def insert(self, string):
        """Insert words into trie tree. Dubplicate will be ignored."""
        if not isinstance(string, str):
            raise TypeError('Input must be a string.')
        step = self.root
        for i in string:
            if i in step.children:
                step = step.children[i]
            else:
                step.children[i] = Node(i)
                step.children[i].parent = step
                step = step.children[i]
        step.end = True
        self._size += 1

    def contains(self, string):
        """Check if string is in trie, return true or false."""
        if not isinstance(string, str):
            raise TypeError('Must provide a string.')
        step = self.root
        for i in string:
            if i in step.children:
                step = step.children[i]
            else:
                return False
        if step.end is True:
            return True
        else:
            return False

    def size(self):
        """Return number of words in trie tree."""
        return self._size

    def remove(self, string):
        """Remove string from trie tree."""
        if not isinstance(string, str):
            raise TypeError('Must provide a string.')
        if not self.contains(string):
            raise ValueError('Word does not exist in tree.')
        step = self.root
        for i in string:
            if i in step.children:
                step = step.children[i]
        if step.end is True:
            while len(step.children) < 2:
                last = step
                step = step.parent
                if step.value == '*':
                    step.children.pop(last.value)
                    return
            step.children.pop(last.value)
            return
