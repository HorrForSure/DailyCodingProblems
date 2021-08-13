# Good morning!
# This is your coding interview problem for today.
# This problem was asked by Google.
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

# Assuming this definition of Node:
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def unival_trees(root):
    def unival_help(node):
        count = 0
        unival = True
        val = node.val
        if (not node.left) & (not node.right):
            a, b = 1, True
        elif not node.right:
            if node.left.val != val:
                unival = False
            a, b = unival_help(node.left)
        elif not node.left:
            if node.right.val != val:
                unival = False
            a, b = unival_help(node.right)
        else:
            a, b = unival_help(node.left)
            c, d = unival_help(node.right)
            a += c
            b = b & d
            if node.left.val == node.right.val == val:
                if b:
                    count += 1
            else:
                unival = False
        count += a
        unival = unival & b
        return count, unival
    total, unival = unival_help(root)
    return total

node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0, Node(0), Node(0))))
print(unival_trees(node))

# On checking the given solution, I can see that it looks cleaner when using a separate function and calling that
# instead, but functionally my solution should provide the same or similar efficiency, as it does not double up
# on the processing of nodes at any point, and delivers the running total unival subtree count up the recursion chain.