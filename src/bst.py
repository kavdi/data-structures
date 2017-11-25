"""Implement binary search tree."""


class Node(object):
    """Structure for a node object."""

    def __init__(self, value, left=None, right=None):
        """Initiate a node object."""
        self.value = value
        self.left = left
        self.right = right


class BST(object):
    """Structure for objects in binary search tree."""

    def __init__(self, iterable=None):
        """Initiate a binary search tree."""
        self.root = None
        self._size = 0
        if isinstance(iterable, (list, tuple)):
            for num in iterable:
                self.insert(num)

    def insert(self, value):
        """Insert value to binary search tree."""
        if not isinstance(value, (int, float)):
            raise ValueError('Please insert number.')

        if self.root is None:
            self.root = Node(value)
            self._size += 1
            return
        elif value == self.root.value:
            raise ValueError('Node already exists.')
        curr = self.root
        while curr:
            if value == curr.value:
                    raise ValueError('Node already exists.')
            elif value > curr.value:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(value)
                    self._size += 1
                    break
            elif value < curr.value:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(value)
                    self._size += 1
                    break

    def search(self, value):
        """Search for value in tree, return node if present, none if not."""
        if self.root is None or not isinstance(value, (int, float)):
            return

        curr = self.root
        while curr:
            if value == curr.value:
                return curr
            elif value > curr.value:
                curr = curr.right
            elif value < curr.value:
                curr = curr.left

    def size(self):
        """Get number of all nodes in bst."""
        return self._size

    def depth(self, root=None):
        """Get depth of levels in bst."""
        if root is None:
            if self.root is None:
                return 0
            else:
                root = self.root
        if not root.right and not root.left:
            return 0
        elif root.right and not root.left:
            return self.depth(root.right) + 1
        elif root.left and not root.right:
            return self.depth(root.left) + 1
        else:
            return max(self.depth(root.right), self.depth(root.left)) + 1

    def contains(self, value):
        """Search for value in bst, return true if there."""
        c = self.search(value)
        if c is None:
            return False
        else:
            return True

    def balance(self):
        """Get the depth of left and right side of bst.

        Return a possitive int if left side is larger, negative int if right side is larger.
        """
        if self.root is None:
            return 'Tree is empty.'
        elif not self.root.left and not self.root.right:
            return 0
        elif self.root.left and not self.root.right:
            return self.depth(self.root.left)
        elif self.root.right and not self.root.left:
            return self.depth(self.root.right)
        else:
            return self.depth(self.root.right) - self.depth(self.root.left)


if __name__ == '__main__':
    import timeit
