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

    def depth(self):
        """Get the depth of bst."""
        if not self.root:
            return "Tree is empty."
        else:
            return self._depth(self.root, -1)

    def _depth(self, curr_node, curr_depth):
        """Recurse through bst until depth is found."""
        if not curr_node:
            return curr_depth
        left_depth = self._depth(curr_node.left, curr_depth + 1)
        right_depth = self._depth(curr_node.right, curr_depth + 1)
        return max(left_depth, right_depth)

    def contains(self, value):
        """Search for value in bst, return true if there."""
        c = self.search(value)
        if c is None:
            return False
        else:
            return True

    def balance(self, node):
        """Get the depth of left and right side of bst.

        Return a possitive int if left side is larger, negative int if right side is larger.
        """
        if node is None:
            return 'Tree is empty.'
        if not node.left and not node.right:
            return 0
        else:
            return self.depth(node.left) - self.depth(node.right)

    def in_order(self):
        """Traverse the bst and yield node values in order."""
        if self.root is None:
            raise ValueError("Tree is empty.")
        curr = self.root
        order = []
        while curr or order:
            if curr:
                order.append(curr)
                curr = curr.left
            else:
                curr = order.pop()
                yield curr.value
                curr = curr.right

    def pre_order(self):
        """Traverse the bst and yield node values in pre order."""
        if self.root is None:
            raise ValueError("Tree is empty.")
        curr = self.root
        order = []
        while curr or order:
            if curr:
                yield curr.value
                if curr.right:
                    order.append(curr.right)
                curr = curr.left
            else:
                curr = order.pop()

    def post_order(self):
        """Traverse the bst and yield node values in post order."""
        if self.root is None:
            raise ValueError("Tree is empty.")
        curr = self.root
        child = None
        order = []
        while curr or order:
            if curr:
                order.append(curr)
                curr = curr.left
            else:
                if order[-1].right and order[-1].right is not child:
                    curr = order[-1].right
                else:
                    child = order.pop()
                    yield child.value

    def breadth_first(self):
        """Traverse the bst breadth first."""
        if self.root is None:
            raise ValueError("Tree is empty.")
        order = [self.root]
        while order:
            curr = order.pop(0)
            if curr.left:
                order.append(curr.left)
            if curr.right:
                order.append(curr.right)
            yield curr.value

    def delete(self, value, root=None):
        """Delete node from bst."""
        if self.root is None:
            return
        root = self.search(value)
        if root.left is None and root.right is None:
            root = None
            return None
        elif root.right is not None:
            new = root.right
            if new.left:
                new = new.left
            else:
                if new.right is None:
                    temp = new
                    new = None
                    root.right, root.left, root = temp.right, temp.left, temp
                    self._size -= 1
                    return None
                else:
                    child = new.right
                    temp = new
                    root.right, root.left, root, temp = temp.right, temp.left, temp, child
                    child = None
                    self._size -= 1
                    return None
        elif root.left is not None:
            new = root.left
            if new.right:
                new = new.right
            else:
                if new.left is None:
                    temp = new
                    new = None
                    root.right, root.left, root = temp.right, temp.left, temp
                    self._size -= 1
                    return None
                else:
                    child = new.left
                    temp = new
                    root.right, root.left, root, temp = temp.right, temp.left, temp, child
                    child = None
                    self._size -= 1
                    return None

    def balance_tree(self):
        """Balance bst left and right sides are close to even as possible."""
        pass

    def create_unbalanced_9_node(self):
        """Create unblanced tree with 7 nodes."""
        self.insert(5)
        self.insert(2)
        self.insert(6)
        self.insert(4)
        self.insert(7)
        self.insert(1)
        self.insert(9)
        self.insert(3)
        self.insert(8)



if __name__ == '__main__':
    import timeit
