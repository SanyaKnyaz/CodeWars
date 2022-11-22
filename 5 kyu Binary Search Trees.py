'''
Binary Search Trees
https://www.codewars.com/kata/571a551a196bb0567f000603
'''
class Tree(object):
    def __init__(self, root, left=None, right=None):
        assert root and isinstance(root, Node)
        assert left is None or isinstance(left, Tree) and left._max().root < root
        assert right is None or isinstance(right, Tree) and root < right._min().root

        self.left = left
        self.root = root
        self.right = right

    def is_leaf(self):
        return not self.left and not self.right

    def _max(self):
        tree = self
        while tree.right:
            tree = tree.right
        return tree

    def _min(self):
        tree = self
        while tree.left:
            tree = tree.left
        return tree

    def __str__(self):
        if self.is_leaf():
            return "[%s]" % self.root
        return "[%s %s %s]" % (
            self.left if self.left else "_",
            self.root,
            self.right if self.right else "_")

    def __eq__(self, other):
        if not other:
            return False
        return (
            self.root == other.root and
            self.left == other.left and
            self.right == other.right)

    def __ne__(self, other):
        return not (self == other)


class Node(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value